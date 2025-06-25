from dotenv import load_dotenv
load_dotenv()
import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL")

if OPENAI_API_KEY is None:
    raise RuntimeError("OPENAI_API_KEY not set. Please provide it in .env.")

