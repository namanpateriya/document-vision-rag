from app.config import CHUNK_SIZE


class DocumentChunker:

    @staticmethod
    def chunk(text: str):

        chunks = []

        start = 0

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk = text[start:end]

            chunks.append(chunk)

            start = end

        return chunks
