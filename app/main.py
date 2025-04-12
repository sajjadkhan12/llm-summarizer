from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from transformers import BartForConditionalGeneration, BartTokenizer
import logging

app = FastAPI(title="Text Summarizer")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model and tokenizer
MODEL_NAME = "facebook/bart-base"
try:
    tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
    model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)
    logger.info(f"Loaded model {MODEL_NAME}")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    raise


class TextInput(BaseModel):
    text: str
    max_length: int = 100
    min_length: int = 30


@app.post("/summarize")
async def summarize(input: TextInput):
    try:
        inputs = tokenizer(
            input.text,
            max_length=1024,
            truncation=True,
            return_tensors="pt"
        )
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=input.max_length,
            min_length=input.min_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return {"summary": summary}
    except Exception as e:
        logger.error(f"Summarization error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health():
    return {"status": "healthy"}