from fastapi import FastAPI

from app.service import DocumentService

app = FastAPI(
    title="Document Vision RAG - Step 1"
)


@app.get("/")
def health():

    return {
        "status": "running"
    }


@app.get("/process")
def process(file_path: str):

    return DocumentService.process(file_path)
