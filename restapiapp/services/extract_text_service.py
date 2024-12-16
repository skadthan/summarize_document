import time
from restapiapp.kafka.producer import publish_event
from restapiapp.utils.logger import get_logger

logger = get_logger(__name__)

def extract_text_srvc(docid: str):
    logger.info(f"Extracting text from {docid}")
    time.sleep(2)  # Simulate processing
    # Dome processing of the uploaded document, like chunkings and save these chunkings for emebeddings retrical.
    extracted_text = f"Extracted sample text from {docid}"
    publish_event("text_extracted", {"docid": docid, "text": extracted_text})
    logger.info("Published text_extracted event")
    return {"error_code": 200, "docid":docid,"message": extracted_text}
