# Generative AI Learning Workspace

Welcome to the **Generative AI Learning Workspace**! This repository is organized modularly, with `generative-ai/` as the root folder and each AI concept, architecture, or project contained within its own dedicated subdirectory.

---

## 📁 Repository Structure

```text
generative-ai/
├── rag/                      # Retrieval-Augmented Generation module
│   ├── main.py               # Interactive CLI RAG chatbot loop with strict prompt rules
│   ├── create_data.py        # PDF document loader, chunker, embedding & ChromaDB storage script
│   ├── test.py               # Benchmark & compare Similarity Search vs. MMR retrieval
│   ├── requirements.txt      # RAG module dependencies
│   ├── README.md             # RAG module documentation
│   ├── documents-loaders/    # Document loading experiments & sample data files
│   └── chroma-db/            # Local persistent Chroma vector database (git-ignored)
│
├── [future-concepts]/        # Additional AI modules (agents, fine-tuning, prompt engineering, etc.)
│
├── requirements.txt          # Root dependency file
├── .env                      # Global environment variables & API keys (git-ignored)
└── README.md                 # Root workspace documentation
```

---

## 🚀 Concept Modules

### 1. 🔍 [Retrieval-Augmented Generation (RAG)](file:///Users/qaiser/Developer/web%20apps/generative-ai/rag/README.md)
Located in [`rag/`](file:///Users/qaiser/Developer/web%20apps/generative-ai/rag/)

- **Capabilities**: Document loading (PDF/text), recursive chunking, vector embeddings with **Mistral AI**, persistent vector database storage with **ChromaDB**, **MMR** retrieval, and grounded RAG chatting.
- **Quick Run**:
  ```bash
  # Index PDF document into ChromaDB
  python rag/create_data.py

  # Test retrieval algorithms
  python rag/test.py

  # Run interactive CLI RAG chatbot
  python rag/main.py
  ```

---

## 🛠️ Quick Start & Setup

### 1. Set Up Virtual Environment

Using `uv`:
```bash
uv venv
source .venv/bin/activate
```

Using standard `venv`:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

Ensure you have a `.env` file at the project root with your API keys:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

---

## 📌 Roadmap / Upcoming Concepts

- [x] **RAG**: Document ingestion, ChromaDB vector store, MMR search, and grounded chatbot.
- [ ] **AI Agents**: LangGraph & agentic workflow orchestration.
- [ ] **Fine-Tuning & Quantization**: PEFT / LoRA fine-tuning workflows.
- [ ] **Multimodal AI**: Image & audio grounding pipelines.
