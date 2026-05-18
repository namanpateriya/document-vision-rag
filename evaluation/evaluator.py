import json
from sentence_transformers import SentenceTransformer
import numpy as np

from app.service import DocumentService

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_similarity(a, b):

    emb = model.encode([a, b])

    return float(
        np.dot(emb[0], emb[1]) /
        (np.linalg.norm(emb[0]) * np.linalg.norm(emb[1]))
    )


def evaluate():

    with open("evaluation/test_cases.json") as f:
        cases = json.load(f)

    results = []

    for case in cases:

        result = DocumentService.process(
            case["file_path"],
            case["query"]
        )

        answer = result.get("answer", "")

        expected = case.get("expected_answer", "")

        similarity = semantic_similarity(answer, expected)

        hallucination = "not found in document" not in answer.lower() and similarity < 0.4

        results.append({
            "id": case["id"],
            "similarity": round(similarity, 3),
            "hallucination": hallucination,
            "passed": similarity > 0.5
        })

        print(case["id"], results[-1])

    return results


if __name__ == "__main__":
    evaluate()
