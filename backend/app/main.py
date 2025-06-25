# backend/app/main.py

import logging
from typing import List
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app import parsing, analysis

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your Next.js origin
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
@app.post("/analyze/")
async def analyze_conversation(
    files: List[UploadFile] = File(...),
    relationship_type: str = Form(...),
    context: str = Form(""),
):
    logger.info("POST /analyze: %d files, relationship_type=%r, context_len=%d",
                len(files), relationship_type, len(context))

    # 1) parse all files
    texts = []
    for f in files:
        try:
            t = await parsing.handle_file_upload(f)
            if t and len(t.strip()) >= 5:
                texts.append(t)
        except Exception:
            logger.exception("Failed to parse %s", f.filename)
    if not texts:
        raise HTTPException(422, "Unable to extract text from uploaded files.")

    full_text = "\n\n".join(texts)

    # 2) run the LLM analysis
    try:
        result = await analysis.run_llm_analysis(full_text, relationship_type, context)
    except Exception:
        logger.exception("run_llm_analysis failed")
        raise HTTPException(500, "Internal analysis error")

    return result
