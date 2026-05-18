import json

from evaluation.evaluator import run


class RAGOptimizer:

    def __init__(self):

        self.recommendations = []

    def analyze(self, results):

        failures = []

        for case in results:

            if not case["passed"]:

                failures.append(case)

                self.generate_recommendation(case)

        return failures

    def generate_recommendation(self, case):

        rec = {
            "id": case["id"],
            "recommendations": []
        }

        rec["recommendations"].append(
            "Improve retrieval relevance (chunking or embeddings)"
        )

        rec["recommendations"].append(
            "Improve prompt grounding for better answers"
        )

        self.recommendations.append(rec)

    def save(self):

        with open(
            "evaluation/optimization_report.json",
            "w"
        ) as f:

            json.dump(
                self.recommendations,
                f,
                indent=2
            )


def optimize():

    results = run() or []

    optimizer = RAGOptimizer()

    failures = optimizer.analyze(results)

    optimizer.save()

    print("\n=== Optimization Summary ===")

    print(f"Failures: {len(failures)}")

    for rec in optimizer.recommendations:

        print(f"\nTest: {rec['id']}")

        for r in rec["recommendations"]:
            print(f"- {r}")


if __name__ == "__main__":
    optimize()
