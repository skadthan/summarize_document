from fastapi import APIRouter
from temporalio.client import Client
from restapiapp.utils.logger import get_logger
import uuid

# Generate a unique workflow ID
workflow_id = f"document-processing-{uuid.uuid4()}"

router = APIRouter()
logger = get_logger(__name__)

@router.post("/start_workflow/")
async def start_workflow(docid: str):
    client = await Client.connect("localhost:7233")
    handle = await client.start_workflow(
        "DocumentProcessingWorkflow",
        docid,
        id=workflow_id,  # Unique workflow ID
        task_queue="document-processing"
    )
    return {"workflow_id": handle.id}