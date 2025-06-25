import pytesseract
from PIL import Image
import pdfplumber
import tempfile
import os
import openai
import base64

async def handle_file_upload(file):
    filename = file.filename.lower()
    # Save file temporarily
    suffix = os.path.splitext(filename)[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    text = ""
    try:
        if suffix in [".txt"]:
            with open(tmp_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
        elif suffix in [".jpg", ".jpeg", ".png", ".webp"]:
            with open(tmp_path, "rb") as img_file:
                img_bytes = img_file.read()
            text = await ocr_with_openai(img_bytes)
        elif suffix in [".pdf"]:
            with pdfplumber.open(tmp_path) as pdf:
                text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        else:
            text = ""  # unsupported
    except Exception as e:
        print(f"[Parse][ERROR] {filename}: {e}")
        text = ""
    finally:
        os.unlink(tmp_path)

    print(f"[Parse] {filename} | Length: {len(text)}")
    return text.strip()

async def ocr_with_openai(img_bytes):
    OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
    client = openai.AsyncOpenAI(api_key=OPENAI_KEY)
    img_b64 = base64.b64encode(img_bytes).decode("utf-8")
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "请帮我识别这张图片中的所有文字内容，直接输出纯文本，不要解释。"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
                ]
            }
        ],
        max_tokens=1024
    )
    return response.choices[0].message.content.strip()
