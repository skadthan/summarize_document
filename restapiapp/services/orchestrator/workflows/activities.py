import requests
from temporalio import activity

@activity.defn
async def fetch_data_from_url(url: str) -> dict:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

@activity.defn
async def extract_text_activity(docid: str):
    response = requests.post("http://ashu.macos:8000/ashu/api/file_process/extract_text/", json={"docid": docid})
    return response.json()["text"]

@activity.defn
async def generate_embeddings_activity(text: str, docid: str):
    response = requests.post("http://ashu.macos:8000/ashu/api/file_process/generate_embeddings/", json={"docid": docid})
    return response.json()["embeddings"]

@activity.defn
async def summarize_text_activity(text: str, docid: str):
    response = requests.post("http://ashu.macos:8000/ashu/api/file_process/summarize_text/", json={"docid": docid})
    return response.json()
