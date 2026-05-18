from app.utils.gemini_client import GeminiClient

client = GeminiClient()


class AnswerGenerator:

    @staticmethod
    def generate(query: str, chunks: list):

        if not chunks:
            return "No relevant information found in document"

        context = "\n\n".join(chunks)

        prompt = f"""
You are an AI assistant for document analysis.

STRICT RULES:
- Use ONLY the provided context
- DO NOT hallucinate
- If answer is not present, say "Not found in document"
- Be precise and concise

Context:
{context}

Question:
{query}

Answer:
"""

        return client.generate(prompt)
