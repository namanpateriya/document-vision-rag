from pydantic import BaseModel


class QueryRequest(BaseModel):

    file_path: str
    query: str


class QueryResponse(BaseModel):

    status: str
    query: str
    answer: str
    retrieved_chunks: list
