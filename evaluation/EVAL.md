# Evaluation

The evaluation framework validates the performance of the document RAG system.

---

# Evaluation Scope

The system evaluates:

- semantic similarity between expected and generated answers
- hallucination detection
- retrieval effectiveness
- end-to-end pipeline behavior

---

# Evaluation Flow

```text
Test Case
    ↓
Document Processing
    ↓
Chunking + Retrieval
    ↓
Answer Generation (Gemini)
    ↓
Semantic Comparison
    ↓
Pass / Fail
```

---

# Metrics

The framework measures:

- semantic similarity score
- hallucination detection
- answer relevance

---

# Running Evaluation

```bash
python -m evaluation.evaluator
```

---

# Running Optimizer

```bash
python -m evaluation.optimizer
```

---

# Optimization Goals

The optimizer identifies:

- low similarity responses
- hallucinated answers
- weak retrieval quality

It provides recommendations for:

- improving prompts
- tuning chunk size
- improving embeddings
- adjusting retrieval strategy

---

# Example Test Case

```json
{
  "file_path": "data/sample.pdf",
  "query": "What is the document about?",
  "expected_answer": "This document provides an overview"
}
```

---

# Limitations

- depends on embedding model quality
- does not use LLM-as-judge (yet)
- limited to single-query evaluation

---

# Future Improvements

- LLM-based evaluation
- retrieval scoring metrics
- latency benchmarking
- multi-query evaluation
- ranking metrics (MRR, Recall@K)

---

# Goal

The goal is to ensure:

- grounded answers
- reliable retrieval
- measurable AI system performance

---

Built for evaluating document-based AI systems.
