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
STAGE_MAX_TOKENS = {
    1: 4000,
    2: 12000,
    3: 20000,
    4: 6000,
    5: 4000,
    6: 16000,
    "distill": 12000,
    "seed": 40000,
    "enrich": 8000,
}
