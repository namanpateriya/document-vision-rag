from app.ingestion.loader import DocumentLoader
from app.ingestion.extractor import DocumentExtractor
from app.ingestion.chunker import DocumentChunker


class DocumentService:

    @staticmethod
    def process(file_path: str):

        file = DocumentLoader.load(file_path)

        text = DocumentExtractor.extract_text(file)

        chunks = DocumentChunker.chunk(text)

        return {
            "status": "success",
            "num_chunks": len(chunks),
            "preview": chunks[:2]
        }
