from fastapi import APIRouter, UploadFile, HTTPException
from celery.result import AsyncResult
from restapiapp.config.settings import UPLOAD_DIR
from restapiapp.utils.file_operations import save_file
from restapiapp.celery_tasks.task_manager import process_document_pipeline
from fastapi import FastAPI, UploadFile
from restapiapp.kafka.producer import publish_event
from restapiapp.utils.logger import get_logger
import aiofiles
import os, uuid

router = APIRouter()
logger = get_logger(__name__)


''' Code for Apache Kafka for asynchronous file processing and using Temporal Workflow Management'''


@router.post("/upload/")
async def upload_file(file: UploadFile):
    try:
        doc_id = uuid.uuid4() # Document ID
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        async with aiofiles.open(file_path, "wb") as out_file:
            content = await file.read()
            await out_file.write(content)
        publish_event("file_uploaded", {"file_path": file_path})
        logger.info(f"Published file_uploaded event for {file_path}")
        return {"error_code": 200, "doc_id": doc_id, "message": "File uploaded successfully", "file_path": file_path}
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        return {"error": str(e)}
    

''''
Code for Rabbit MQ using Celery

@router.post("/upload/")
async def upload_document(file: UploadFile):
    try:
        file_path = await save_file(file, UPLOAD_DIR)
        task = process_document_pipeline.delay(file.filename, file_path)
        return {"document_id": task.id, "message": "Document uploaded and processing started."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status/{document_id}/")
async def check_status(document_id: str):
    task_result = AsyncResult(document_id)
    return {
        "document_id": document_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None
    }
'''