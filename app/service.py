from app.ingestion.loader import DocumentLoader
from app.ingestion.extractor import DocumentExtractor
from app.ingestion.chunker import DocumentChunker

from app.retrieval.embeddings import embed_texts
from app.retrieval.vector_store import VectorStore
from app.retrieval.retriever import Retriever


class DocumentService:

    @staticmethod
    def process(file_path: str, query: str):

        # Step 1: Load
        file = DocumentLoader.load(file_path)

        # Step 2: Extract
        text = DocumentExtractor.extract_text(file)

        # Step 3: Chunk
        chunks = DocumentChunker.chunk(text)

        # Step 4: Embed
        embeddings = embed_texts(chunks)

        # Step 5: Store
        store = VectorStore()
        store.build(embeddings, chunks)

        # Step 6: Retrieve
        retriever = Retriever(store)
        results = retriever.retrieve(query)

        return {
            "status": "success",
            "query": query,
            "retrieved_chunks": results
        }
