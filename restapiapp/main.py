from fastapi import FastAPI
from restapiapp.routers import auth, upload_file, temporal_orchestrator,extract_text,generate_embeddings,summarize_text

app = FastAPI(root_path="/ashu/api")
app.include_router(auth.router,prefix="/auth", tags=["Authentication"])
app.include_router(upload_file.router,prefix="/file", tags=["File Upload"])
app.include_router(temporal_orchestrator.router, prefix="/temporal/file_process",tags=["Temporal Workflows"])
app.include_router(extract_text.router,prefix="/file_process",tags=["File Processing"])
app.include_router(generate_embeddings.router,prefix="/file_process",tags=["Embeddings"])
app.include_router(summarize_text.router,prefix="/file_process",tags=["Text Summarization"])



@app.get("/")
async def root():
    return {"message": "Welcome to high concurrent embedding services!"}
