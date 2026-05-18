from fastapi import FastAPI

from app.service import DocumentService

app = FastAPI(title="Document Vision RAG")


@app.get("/")
def health():
    return {"status": "running"}


@app.get("/ask")
def ask(file_path: str, query: str):

    if not file_path:
        return {"status": "error", "message": "file_path required"}

    if not query:
        return {"status": "error", "message": "query required"}

    return DocumentService.process(file_path, query)
