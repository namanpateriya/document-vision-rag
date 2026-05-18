from app.ingestion.loader import DocumentLoader
from app.ingestion.extractor import DocumentExtractor
from app.ingestion.chunker import DocumentChunker

from app.retrieval.embeddings import embed_texts
from app.retrieval.vector_store import VectorStore
from app.retrieval.retriever import Retriever

from app.generation.answer_generator import AnswerGenerator

from app.utils.logger import get_logger

logger = get_logger(__name__)


class DocumentService:

    @staticmethod
    def process(file_path: str, query: str):

        if not query or not query.strip():
            return {
                "status": "error",
                "message": "empty query"
            }

        try:

            file = DocumentLoader.load(file_path)

            text = DocumentExtractor.extract_text(file)

            if not text.strip():
                return {
                    "status": "error",
                    "message": "empty document"
                }

            chunks = DocumentChunker.chunk(text)

            embeddings = embed_texts(chunks)

            store = VectorStore()
            store.build(embeddings, chunks)

            retriever = Retriever(store)

            retrieved = retriever.retrieve(query)

            if not retrieved:
                return {
                    "status": "success",
                    "query": query,
                    "answer": "No relevant information found in document",
                    "retrieved_chunks": []
                }

            answer = AnswerGenerator.generate(query, retrieved)

            if answer.startswith("error:"):
                return {
                    "status": "error",
                    "message": answer
                }

            return {
                "status": "success",
                "query": query,
                "answer": answer,
                "retrieved_chunks": retrieved
            }

        except Exception as e:

            logger.error(f"Processing failed: {e}")

            return {
                "status": "error",
                "message": str(e)
            }
