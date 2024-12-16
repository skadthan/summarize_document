from fastapi import APIRouter
from restapiapp.utils.logger import get_logger
from restapiapp.kafka.consumer import get_consumer
from restapiapp.services.generate_embeddings_service import generate_embeddings_srvc


router = APIRouter()
logger = get_logger(__name__)

@router.post("/generate_embeddings/")
async def generate_embeddings(docid: str):
    consumer = get_consumer("text_extracted", "generate_embeddings_service")
    for message in consumer:
        docid = message.value["docid"]
        response = generate_embeddings_srvc(docid)
    return response