from temporalio import workflow
#from restapiapp.services.orchestrator.workflows.activities import (extract_text_activity, generate_embeddings_activity, summarize_text_activity)


@workflow.defn
class DocumentProcessingWorkflow:
    @workflow.run
    async def run(self, file_path: str):
        text = await workflow.execute_activity("extract_text_activity", file_path)
        embeddings = await workflow.execute_activity("generate_embeddings_activity", text)
        summary = await workflow.execute_activity("summarize_text_activity", text)
        return {"text": text, "embeddings": embeddings, "summary": summary}