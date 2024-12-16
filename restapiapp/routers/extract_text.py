from fastapi import APIRouter
from restapiapp.utils.logger import get_logger
from restapiapp.kafka.consumer import get_consumer
from restapiapp.services.extract_text_service import extract_text_srvc
from restapiapp.models.auth_models import ExtractTextRequest


router = APIRouter()
logger = get_logger(__name__)

@router.post("/extract_text/")
async def extract_text(request: ExtractTextRequest):
    consumer = get_consumer("file_uploaded", "extract_text_service")
    for message in consumer:
        print("print whole kafka message", message)
        kafka_message_value = message.value[request.docid]
        print("kafka_message request.docid", kafka_message_value )
        response = extract_text_srvc(request.docid)
    return response