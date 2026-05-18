from app.utils.gemini_client import GeminiClient

client = GeminiClient()


class AnswerGenerator:

    @staticmethod
    def generate(query: str, chunks: list):

        context = "\n\n".join(chunks)

        prompt = f"""
You are an AI assistant for document analysis.

STRICT RULES:
- Use ONLY the provided context
- Do NOT hallucinate
- If answer not present, say "Not found in document"
- Be concise and precise

Context:
{context}

Question:
{query}

Answer:
"""

        response = client.generate(prompt)

        return response
