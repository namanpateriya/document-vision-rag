import re

from app.config import CHUNK_SIZE


class DocumentChunker:

    @staticmethod
    def chunk(text: str):

        sentences = re.split(r'(?<=[.!?]) +', text)

        chunks = []
        current = ""

        for sentence in sentences:

            if len(current) + len(sentence) < CHUNK_SIZE:
                current += " " + sentence
            else:
                chunks.append(current.strip())
                current = sentence

        if current:
            chunks.append(current.strip())

        return chunks
