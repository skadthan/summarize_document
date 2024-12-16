import time
from restapiapp.kafka.producer import publish_event
from restapiapp.utils.logger import get_logger

logger = get_logger(__name__)

def summarize_text_srvc(docid: str):
    logger.info("Summarizing text...")
    time.sleep(2)
    summary = {"summary": "This is a summary", "keywords": ["keyword1", "keyword2"]}
    publish_event("summary_generated", {"docid": docid, "summary": summary})
    logger.info("Published summary_generated event")
    return {"error_code": 200,"docid":docid, "message": summary}
