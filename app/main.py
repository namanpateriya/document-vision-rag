from fastapi import FastAPI

from app.service import DocumentService

app = FastAPI(
    title="Document Vision RAG - Step 2"
)


@app.get("/")
def health():
    return {"status": "running"}


@app.get("/query")
def query(file_path: str, query: str):

    return DocumentService.process(
        file_path,
        query
    )
