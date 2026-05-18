from evaluation.evaluator import evaluate


def optimize():

    results = evaluate()

    issues = {
        "low_similarity": 0,
        "hallucination": 0
    }

    for r in results:

        if r["similarity"] < 0.5:
            issues["low_similarity"] += 1

        if r["hallucination"]:
            issues["hallucination"] += 1

    print("\n=== OPTIMIZATION REPORT ===")

    print(f"Low Similarity Cases: {issues['low_similarity']}")
    print(f"Hallucinations: {issues['hallucination']}")

    if issues["hallucination"] > 0:
        print("\nRecommendation:")
        print("- Strengthen prompt grounding")
        print("- Reduce chunk size")
        print("- Improve retrieval relevance")

    if issues["low_similarity"] > 0:
        print("\nRecommendation:")
        print("- Improve embeddings")
        print("- Tune chunking strategy")
        print("- Increase top_k retrieval")


if __name__ == "__main__":
    optimize()
