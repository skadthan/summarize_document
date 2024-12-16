from temporalio.worker import Worker
from restapiapp.services.orchestrator.workflows.workflows import DocumentProcessingWorkflow
from restapiapp.services.orchestrator.workflows.activities import extract_text_activity, generate_embeddings_activity, summarize_text_activity
from temporalio.client import Client
import asyncio


async def run_worker():
    client = await Client.connect("localhost:7233")
    print("temporal  client", client)
    worker = Worker(
        client,
        task_queue="document-processing",
        workflows=[DocumentProcessingWorkflow],
        activities=[extract_text_activity, generate_embeddings_activity, summarize_text_activity],
    )
    await worker.run()

if __name__ == "__main__":
    asyncio.run(run_worker())

