# Architecture

## Overview

Document Vision RAG is a lightweight AI system for understanding and querying documents using retrieval-augmented generation.

---

# Core Flow

```text
Document → Extract → Chunk → Embed → Retrieve → Generate Answer
```

---

# System Components

## Ingestion Layer

- loads PDF documents
- extracts raw text

## Chunking Layer

- splits text into manageable segments

## Embedding Layer

- converts chunks into vector representations

## Vector Store

- FAISS-based similarity search

## Retrieval Layer

- fetches top relevant chunks

## Generation Layer

- Gemini generates grounded answers

---

# Data Flow

```text
PDF
 ↓
Extractor
 ↓
Chunker
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

# Design Principles

- modular architecture
- deterministic retrieval
- grounded answer generation
- lightweight implementation

---

# Limitations

- no OCR support
- basic evaluation
- single-document processing

---

# Future Enhancements

- multi-document retrieval
- semantic evaluation
- UI interface
- OCR integration
- streaming responses

---

# Summary

This repository demonstrates:

```text
end-to-end document understanding system using RAG + Gemini
```
