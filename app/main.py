from fastapi import FastAPI

from app.service import DocumentService

app = FastAPI(
    title="Document Vision RAG"
)


@app.get("/")
def health():
    return {"status": "running"}


@app.get("/ask")
def ask(file_path: str, query: str):

    return DocumentService.process(
        file_path,
        query
    )
