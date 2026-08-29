# Retrieval-Augmented Generation (RAG) Module

This directory contains the hands-on implementation and experiments for **Retrieval-Augmented Generation (RAG)** using **LangChain**, **Mistral AI**, and **ChromaDB**.

---

## 📁 Module Structure

```text
rag/
├── main.py                   # Interactive CLI RAG chatbot loop with strict prompt rules
├── create_data.py            # PDF document loader, chunker, embedding & ChromaDB storage script
├── test.py                   # Benchmark & compare Similarity Search vs. MMR retrieval
├── requirements.txt          # Module dependencies (LangChain, ChromaDB, Mistral, etc.)
├── README.md                 # Module documentation
├── documents-loaders/        # Document loader experiments & sample data
│   ├── pdf.py                # PDF document loading & chunking experiment
│   ├── test.py               # TextLoader & CharacterTextSplitter test script
│   ├── notes.txt             # Text sample for loader tests
│   └── wren_and_martin.pdf   # Reference PDF document indexed into vector database
└── chroma-db/                # Persistent vector database directory (git-ignored)
```

---

## ⚙️ Quick Start

### 1. Ingest Documents & Create Vector Embeddings

```bash
python rag/create_data.py
```
*(Or from within `rag/` directory: `python create_data.py`)*

### 2. Run Retrieval Experiments (Similarity vs. MMR)

```bash
python rag/test.py
```

### 3. Launch Interactive Grounded RAG Chatbot

```bash
python rag/main.py
```

- Type your prompt when prompted (`You : ...`).
- Enter `0` to quit the session.

---

## 🎯 Key Features & Design

1. **Document Loading**: Extract text using `PyPDFLoader` and `TextLoader`.
2. **Text Chunking**: Segment text via `RecursiveCharacterTextSplitter` (`chunk_size=1000`, `chunk_overlap=200`).
3. **Embeddings & Persistence**: Generate vector embeddings using `MistralAIEmbeddings` (`mistral-embed`) and store them in `ChromaDB`.
4. **Diversity Retrieval**: Use MMR (Maximal Marginal Relevance) retrieval (`k=4`, `fetch_k=10`, `lambda_mult=0.5`) to eliminate redundant matches.
5. **Strict Grounding**: System prompt strictly enforces context-based answers only, outputting `"I could not find the answer in the document."` if context is missing.
