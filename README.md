# Document Vision RAG

Document Vision RAG is a lightweight AI system for understanding and querying documents using retrieval-augmented generation.

It enables:
- document ingestion (PDF)
- semantic retrieval over document content
- grounded answer generation using Google Gemini
- evaluation and optimization of RAG workflows

---

# Features

- PDF document ingestion and text extraction
- Semantic chunking and embedding
- FAISS-based vector retrieval
- Context-grounded answer generation
- Semantic evaluation (not just keyword matching)
- Hallucination detection
- Optimization recommendations engine
- CLI and API-based usage

---

# Why This Repository

Modern AI systems are evolving from:

```text
text generation
```

to:

```text
retrieval + reasoning + evaluation
```

This repository demonstrates how to build AI systems that are:
- grounded in data
- measurable
- debuggable
- improvable

---

# Architecture Overview

```text
Document
 ↓
Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Store
 ↓
Retriever
 ↓
Gemini
 ↓
Answer
```

---

# Setup

Clone repository:

```bash
git clone <repo_url>
cd document-vision-rag
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```text
GEMINI_API_KEY=your_key
MODEL_NAME=gemini-1.5-flash
```

---

# API Usage

Start server:

```bash
uvicorn app.main:app --reload
```

Endpoint:

```text
GET /ask?file_path=data/sample.pdf&query=your_query
```

---

# CLI / Testing

Example:

```text
http://127.0.0.1:8000/ask?file_path=data/sample.pdf&query=Summarize the document
```

---

# Evaluation & Optimization

This repository includes an advanced evaluation framework for RAG systems.

It evaluates:
- semantic similarity between expected and generated answers
- hallucination detection
- retrieval effectiveness

Run evaluation:

```bash
python -m evaluation.evaluator
```

Run optimization:

```bash
python -m evaluation.optimizer
```

This enables:

```text
Build → Evaluate → Optimize
```

---

# Engineering Highlights

- Modular RAG architecture
- Deterministic retrieval layer (FAISS)
- Grounded answer generation
- Semantic evaluation engine
- Optimization feedback loop
- Google Gemini integration

---

# Google Ecosystem Alignment

This repository is built using Google Gemini and aligns with modern Google AI workflows.

It demonstrates:
- retrieval-augmented generation
- grounded reasoning
- document understanding workflows
- structured AI system design

Inspired by:
- Google Gemini Cookbook
- Google AI Studio
- modern Google GenAI patterns

---

# Use Cases

- contract analysis
- document summarization
- compliance review
- knowledge base querying
- enterprise document AI

---

# Limitations

- evaluation depends on embedding quality
- single-document processing
- no OCR support
- no UI interface

---

# Future Enhancements

- multi-document retrieval
- reranking (hybrid search)
- OCR pipelines
- UI interface
- streaming responses

---

# Design Philosophy

This repository is intentionally designed as:

```text
small, modular, and production-minded AI system
```

focusing on:
- clarity
- reliability
- evaluation
- real-world usability

---

Built using Google Gemini for modern document AI systems.
