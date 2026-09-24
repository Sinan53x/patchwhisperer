import os

from dotenv import load_dotenv

load_dotenv()

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.commandcode.ai/provider/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "deepseek/deepseek-v4-flash")
CMDC_API_KEY = os.getenv("CMDC_API_KEY", "")

# placeholder pricing ($/1M tokens) until real rates are known
PRICE_INPUT_PER_M = 0.30
PRICE_OUTPUT_PER_M = 1.20

DEFAULT_POOL = os.getenv("DEFAULT_POOL", "")

# per-stage output token budgets
# reasoning models spend a variable, often large share of max_tokens on hidden
# reasoning before emitting JSON, so budgets include generous headroom for it
STAGE_MAX_TOKENS = {
    1: 24000,
    2: 32000,
    3: 48000,
    4: 24000,
    5: 24000,
    6: 32000,
    "6h": 32000,
    "distill": 32000,
    "seed": 60000,
    "enrich": 24000,
}

STAGE6_HERO_BATCH = 10
