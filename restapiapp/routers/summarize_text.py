from fastapi import APIRouter
from restapiapp.utils.logger import get_logger
from restapiapp.kafka.consumer import get_consumer
from restapiapp.services.summarize_text_service import summarize_text_srvc


router = APIRouter()
logger = get_logger(__name__)

@router.post("/summarize_text/")
async def start_workflow(docid: str):
    consumer = get_consumer("text_extracted", "generate_embeddings_service")
    for message in consumer:
        file_path = message.value["docid"]
        response = summarize_text_srvc(docid)
    return response