import numpy as np
import faiss

from app.utils.logger import get_logger

logger = get_logger(__name__)


class VectorStore:

    def __init__(self):

        self.index = None
        self.text_chunks = []

    def build(self, embeddings, chunks):

        embeddings = np.array(
            embeddings
        ).astype("float32")

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(embeddings)

        self.text_chunks = chunks

        logger.info(
            f"Vector store built with {len(chunks)} chunks"
        )

    def search(self, query_embedding, top_k=3):

        if self.index is None:

            return []

        query_embedding = np.array(
            query_embedding
        ).astype("float32")

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:

            if 0 <= idx < len(self.text_chunks):

                results.append(
                    self.text_chunks[idx]
                )

        return results
