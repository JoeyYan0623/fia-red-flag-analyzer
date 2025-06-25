# backend/app/analysis.py
import os
import logging
import json
from dotenv import load_dotenv
from openai import AsyncOpenAI
from .fia_data import UNES_TRAITS, PLAYER_TYPES

load_dotenv()
logger = logging.getLogger(__name__)

OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment variables.")

llm = AsyncOpenAI(api_key=OPENAI_KEY)


def build_trait_rubric() -> str:
    lines = []
    for trait, info in UNES_TRAITS.items():
        desc = info["description"]
        scores = info["scores"]
        lines.append(
            f"{trait} ({desc})  →  0={scores[0]}; 2={scores[2]}; 5={scores[5]}; 8={scores[8]}; 10={scores[10]}"
        )
    return "\n".join(lines)


def build_player_reference() -> str:
    # build a bullet list of each key, name, and one-line descriptor
    bullets = []
    for key, p in PLAYER_TYPES.items():
        bullets.append(f"- **{key}**: {p['name']} — {p['description']}")
    return "\n".join(bullets)


RUBRIC_TEXT = build_trait_rubric()
PLAYER_REF = build_player_reference()


async def llm_trait_scoring(conversation: str, relationship: str) -> dict:
    system = f"""
You are a relationship expert.  Use _only_ the UNES rubric below to score exactly 30 traits.
Then, based solely on those scores, pick _one_ best-matching player type key.

--- UNES RUBRIC ---
{RUBRIC_TEXT}

--- AVAILABLE PLAYER TYPES (key: name — description) ---
{PLAYER_REF}

**RETURN A JSON OBJECT WITH EXACT FIELDS**:
1. trait_scores    (object of 30 integer scores)
2. conversation_analysis   (2–4 sentence summary)
3. conversation_tips       (array of 3 bullet-style tips)
4. player_type_guess       (one of the keys above)
5. player_type_reasoning   (one sentence)

Respond with _only_ that JSON.  Do not wrap it, do not add extra keys.
    """

    user = f"""
Conversation context (relationship = "{relationship}"):

\"\"\"
{conversation}
\"\"\"
    """

    resp = await llm.chat.completions.create(
        model="gpt-4o",
        temperature=0.0,
        max_tokens=800,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": user},
        ],
    )
    raw = resp.choices[0].message.content
    logger.info("[LLM1 OUTPUT] %s", raw)

    try:
        return json.loads(raw)
    except Exception as e:
        logger.error("Failed to parse LLM1 JSON: %s", e)
        return {}


async def llm_player_type_verification(trait_scores: dict, guess: str) -> dict:
    system = f"""
You are a UNES relationship expert verifying someone’s classification.
Here are the same player types, with their HIGH and LOW traits:

{PLAYER_REF}

**GIVEN**:
{{ "player_type_guess": "{guess}", "trait_scores": {trait_scores} }}

**RETURN A JSON OBJECT WITH EXACT FIELDS**:
- final_player_type  (key)
- reasoning           (one sentence why this is correct or why we change it)
- victim_emotions     (array of 3–5 emotions typical for that type)
- summary             (one-sentence description of dynamic)

Respond with _only_ that JSON.  No extra keys.
    """

    resp = await llm.chat.completions.create(
        model="gpt-4o",
        temperature=0.0,
        max_tokens=400,
        response_format={"type": "json_object"},
        messages=[{"role": "system", "content": system}],
    )
    raw = resp.choices[0].message.content
    logger.info("[LLM2 OUTPUT] %s", raw)

    try:
        return json.loads(raw)
    except Exception as e:
        logger.error("Failed to parse LLM2 JSON: %s", e)
        return {}


async def run_llm_analysis(conversation: str, relationship: str, context: str = "") -> dict:
    """
    1) Trait scoring + initial player guess
    2) Verify & possibly correct guess
    """

    text = f"{context}\n\n{conversation}" if context else conversation

    # STEP 1
    first = await llm_trait_scoring(text, relationship)
    if "trait_scores" not in first:
        raise RuntimeError("LLM1 did not return trait_scores.")
    scores = first["trait_scores"]
    guess  = first.get("player_type_guess", "no_red_flags")

    # STEP 2
    verify = await llm_player_type_verification(scores, guess)
    final = verify.get("final_player_type", guess)

    return {
        "trait_scores": scores,
        "conversation_analysis": first.get("conversation_analysis", ""),
        "conversation_tips": first.get("conversation_tips", []),
        "player_type": final,
        "player_type_reasoning": verify.get("reasoning", ""),
        "player_type_summary": verify.get("summary", ""),
        "victim_emotions": verify.get("victim_emotions", []),
    }
