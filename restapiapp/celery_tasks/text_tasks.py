from celery import Celery
from restapiapp.utils.logger import get_logger
import time
from restapiapp.config.settings import BROKER_URL, RESULT_BACKEND

logger = get_logger(__name__)
celery = Celery('tasks', broker=BROKER_URL, backend=RESULT_BACKEND)

@celery.task
def extract_text(file_path):
    logger.info(f"Extracting text from: {file_path}")
    time.sleep(2)  # Simulate processing delay
    return f"Extracted text from {file_path}"

@celery.task
def generate_embeddings(text):
    logger.info(f"Generating embeddings for text: {text[:20]}...")
    time.sleep(2)  # Simulate processing delay
    return {"embeddings": "Vectorized representation"}


@celery.task
def summarize_text(text):
    logger.info(f"Summarizing text: {text[:20]}...")
    time.sleep(2)  # Simulate processing delay
    return {"summary": "Text summary", "keywords": ["keyword1", "keyword2"]}