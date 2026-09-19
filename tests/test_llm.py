import json

import pytest
from pydantic import BaseModel

from patchwhisperer.analysis.llm import FakeLLMClient, LLMClient, extract_json


class M(BaseModel):
    x: int


def test_extract_plain():
    assert json.loads(extract_json('{"x": 1}')) == {"x": 1}


def test_extract_fenced():
    assert json.loads(extract_json('sure!\n```json\n{"x": 2}\n```\ndone')) == {"x": 2}


def test_extract_embedded():
    assert json.loads(extract_json('pre {"x": 3} post')) == {"x": 3}


def test_fake_client():
    llm = FakeLLMClient({"# Task: systems analysis": {"x": 5}})
    out = llm.complete_json("sys", "blah\n# Task: systems analysis\nblah", M)
    assert out.x == 5


def test_validation_retry(monkeypatch):
    calls = []

    class FakeCompletions:
        def create(self, **kw):
            calls.append(kw["messages"])
            if len(calls) == 1:
                content = "not json"
            else:
                content = '{"x": 7}'
            return type(
                "R",
                (),
                {
                    "usage": type(
                        "U", (), {"prompt_tokens": 10, "completion_tokens": 5}
                    ),
                    "choices": [
                        type(
                            "C",
                            (),
                            {"message": type("Msg", (), {"content": content})},
                        )
                    ],
                },
            )()

    def fake_init(self, **kw):
        self.model = "fake"
        self.usage = {"prompt_tokens": 0, "completion_tokens": 0}

    monkeypatch.setattr(LLMClient, "__init__", fake_init)
    llm = LLMClient()
    llm.client = type(
        "C", (), {"chat": type("Ch", (), {"completions": FakeCompletions()})}
    )()
    out = llm.complete_json("sys", "user", M)
    assert out.x == 7
    assert len(calls) == 2
    assert "Return only the corrected JSON" in calls[1][-1]["content"]
    assert llm.usage == {"prompt_tokens": 20, "completion_tokens": 10}


def test_validation_failure_raises(monkeypatch):
    class FakeCompletions:
        def create(self, **kw):
            return type(
                "R",
                (),
                {
                    "usage": None,
                    "choices": [
                        type("C", (), {"message": type("Msg", (), {"content": "bad"})})
                    ],
                },
            )()

    def fake_init(self, **kw):
        self.model = "fake"
        self.usage = {"prompt_tokens": 0, "completion_tokens": 0}

    monkeypatch.setattr(LLMClient, "__init__", fake_init)
    llm = LLMClient()
    llm.client = type(
        "C", (), {"chat": type("Ch", (), {"completions": FakeCompletions()})}
    )()
    with pytest.raises(RuntimeError):
        llm.complete_json("sys", "user", M, retries=1)
