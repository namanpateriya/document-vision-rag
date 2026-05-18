# Evaluation

This repository includes an evaluation framework for validating document-based RAG workflows.

---

# Evaluation Scope

The system evaluates:

- retrieval relevance
- answer grounding
- response correctness (basic)
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
Gemini Answer Generation
    ↓
Keyword Matching
    ↓
Pass / Fail
```

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

# Metrics

Currently measured:

- keyword presence
- answer relevance (basic)
- pipeline success

---

# Limitations

- keyword-based validation
- no semantic scoring
- no hallucination detection

---

# Future Improvements

- semantic similarity scoring
- LLM-as-a-judge evaluation
- retrieval quality scoring
- latency tracking
- multi-query evaluation

---

# Goal

The goal is to ensure:

- reliable document understanding
- grounded answers
- consistent RAG behavior

---

Built for evaluating lightweight document AI systems.
