import time
from restapiapp.kafka.producer import publish_event
from restapiapp.utils.logger import get_logger

logger = get_logger(__name__)

def generate_embeddings_srvc(text: str):
    logger.info("Generating embeddings...")
    time.sleep(2)
    embeddings = {"embeddings": f"Embeddings for '{text[:20]}'"}
    publish_event("embeddings_generated", {"text": text, "embeddings": embeddings})
    logger.info("Published embeddings_generated event")
    return {"error_code": 200, "message": embeddings}
