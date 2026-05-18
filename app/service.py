from app.ingestion.loader import DocumentLoader
from app.ingestion.extractor import DocumentExtractor
from app.ingestion.chunker import DocumentChunker

from app.retrieval.embeddings import embed_texts
from app.retrieval.vector_store import VectorStore
from app.retrieval.retriever import Retriever

from app.generation.answer_generator import AnswerGenerator


class DocumentService:

    @staticmethod
    def process(file_path: str, query: str):

        try:

            # Load
            file = DocumentLoader.load(file_path)

            # Extract
            text = DocumentExtractor.extract_text(file)

            # Chunk
            chunks = DocumentChunker.chunk(text)

            # Embed
            embeddings = embed_texts(chunks)

            # Store
            store = VectorStore()
            store.build(embeddings, chunks)

            # Retrieve
            retriever = Retriever(store)
            retrieved = retriever.retrieve(query)

            # Generate Answer
            answer = AnswerGenerator.generate(
                query,
                retrieved
            )

            return {
                "status": "success",
                "query": query,
                "answer": answer,
                "retrieved_chunks": retrieved
            }

        except Exception as e:

            return {
                "status": "error",
                "message": str(e)
            }
