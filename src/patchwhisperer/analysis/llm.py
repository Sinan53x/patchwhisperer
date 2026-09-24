import json
import logging
import re
from pathlib import Path

import openai
from pydantic import BaseModel, ValidationError

from patchwhisperer.config import CMDC_API_KEY, LLM_BASE_URL, LLM_MODEL

log = logging.getLogger(__name__)

PROMPTS_DIR = Path(__file__).parent / "prompts"
SYSTEM_PROMPT = (PROMPTS_DIR / "system.md").read_text()


def load_prompt(name: str) -> str:
    return (PROMPTS_DIR / f"{name}.md").read_text()


def render_prompt(name: str, **values: str) -> str:
    text = load_prompt(name)
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", str(value))
    return text


def extract_json(text: str) -> str:
    text = text.strip()
    fence = re.search(r"```(?:json)?\s*(.*?)```", text, re.DOTALL)
    if fence:
        text = fence.group(1).strip()
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end > start:
        text = text[start : end + 1]
    return text


class LLMClient:
    def __init__(
        self,
        base_url: str = LLM_BASE_URL,
        api_key: str = CMDC_API_KEY,
        model: str = LLM_MODEL,
    ) -> None:
        self.model = model
        self.client = openai.OpenAI(
            base_url=base_url, api_key=api_key, timeout=300, max_retries=3
        )
        self.usage: dict[str, int] = {"prompt_tokens": 0, "completion_tokens": 0}

    def _call(self, messages: list[dict], temperature: float, max_tokens: int):
        try:
            return self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                response_format={"type": "json_object"},
            )
        except openai.BadRequestError:
            return self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )

    def complete_json(
        self,
        system: str,
        user: str,
        schema: type[BaseModel],
        *,
        temperature: float = 0.2,
        max_tokens: int = 8000,
        retries: int = 2,
        raw_path: Path | None = None,
    ) -> BaseModel:
        stage_label = user.splitlines()[0] if user else "?"
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]
        last_err: Exception | None = None
        truncated_retried = False
        for attempt in range(retries + 1):
            resp = self._call(messages, temperature, max_tokens)
            if resp.usage:
                self.usage["prompt_tokens"] += resp.usage.prompt_tokens or 0
                self.usage["completion_tokens"] += resp.usage.completion_tokens or 0
                details = getattr(resp.usage, "completion_tokens_details", None)
                log.info(
                    "llm usage: %s in / %s out (%s reasoning)",
                    resp.usage.prompt_tokens,
                    resp.usage.completion_tokens,
                    getattr(details, "reasoning_tokens", None),
                )
            if resp.choices[0].finish_reason == "length":
                if raw_path:
                    raw_path.write_text(
                        resp.choices[0].message.content or ""
                    )
                if truncated_retried:
                    raise RuntimeError(
                        f"output truncated at {max_tokens} tokens ({stage_label})"
                    )
                truncated_retried = True
                max_tokens = min(max_tokens * 2, 60000)
                log.warning(
                    "%s: output truncated, retrying with max_tokens=%d",
                    stage_label,
                    max_tokens,
                )
                continue
            text = resp.choices[0].message.content or ""
            try:
                return schema.model_validate_json(extract_json(text))
            except (ValidationError, json.JSONDecodeError) as e:
                last_err = e
                log.warning("stage validation failed (attempt %d): %s", attempt + 1, e)
                if raw_path:
                    raw_path.write_text(text)
                messages = messages + [
                    {"role": "assistant", "content": text},
                    {
                        "role": "user",
                        "content": f"{e}\nReturn only the corrected JSON.",
                    },
                ]
        raise RuntimeError(f"LLM output failed validation after retries: {last_err}")


class FakeLLMClient:
    """Test double: returns canned JSON keyed by the '# Task:' marker in the prompt."""

    def __init__(self, canned: dict[str, str | dict]) -> None:
        self.canned = canned
        self.usage = {"prompt_tokens": 0, "completion_tokens": 0}
        self.calls: list[str] = []

    def complete_json(
        self, system: str, user: str, schema: type[BaseModel], **kwargs
    ) -> BaseModel:
        for marker, payload in self.canned.items():
            if marker in user:
                self.calls.append(marker)
                raw = payload if isinstance(payload, str) else json.dumps(payload)
                return schema.model_validate_json(raw)
        raise KeyError(f"no canned response for prompt: {user[:80]}")


def stage_marker(stage: str) -> str:
    """The '# Task:' first line of a prompt, used as the FakeLLMClient key."""
    return load_prompt(stage).splitlines()[0]
