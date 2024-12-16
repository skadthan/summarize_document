from celery import Celery
from restapiapp.celery_tasks.text_tasks import extract_text, generate_embeddings, summarize_text
from restapiapp.config.settings import BROKER_URL, RESULT_BACKEND
import logging
from celery import chain

logger = logging.getLogger(__name__)
celery = Celery('tasks', broker=BROKER_URL, backend=RESULT_BACKEND)

@celery.task
def process_document_pipeline(filename, file_path):
    """
    Chain tasks for document processing pipeline:
    1. Extract text
    2. Generate embeddings
    3. Summarize text
    """
    return chain(
        extract_text.s(filename, file_path),
        generate_embeddings.s(),
        summarize_text.s()
    )