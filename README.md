# 🤖 Smart AI Assistant

A Full-Stack AI Assistant built using **React.js**, **FastAPI**, **PostgreSQL**, **ChromaDB**, and **Qwen LLM**. The application supports intelligent conversations, memory-based interactions, AI tools, chat history, and PDF-based Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

* AI Chat Assistant
* Multi-Session Chat History
* Memory-Based Conversations
* PDF Upload
* Retrieval-Augmented Generation (RAG)
* ChromaDB Vector Database
* Weather Tool
* Search Tool
* Calculator Tool
* Travel Tool
* PostgreSQL Database
* FastAPI Backend
* React Frontend

---

## 🏗️ Architecture

```text
User
   ↓
React Frontend
   ↓
FastAPI Backend
   ↓
Memory & Tool Routing
   ↓
RAG Retrieval (ChromaDB)
   ↓
Qwen LLM
   ↓
AI Response
```

---

## 🧠 RAG Workflow

```text
PDF Upload
      ↓
Extract Text
      ↓
Chunking
      ↓
Generate Embeddings
      ↓
Store in ChromaDB
      ↓
User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Retrieve Relevant Chunks
      ↓
Context + Qwen
      ↓
Generate Answer
```

---

## 🛠️ Tech Stack

### Frontend

* React.js
* Tailwind CSS
* Vite

### Backend

* Python
* FastAPI

### Database

* PostgreSQL
* ChromaDB

### AI

* Qwen LLM
* LangChain
* Embedding Model

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-ai-assistant.git
cd smart-ai-assistant
```

### Backend

```bash
pip install -r requirements.txt
python main.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 📌 Future Improvements

* Docker Support
* Project Deployment
* User Authentication
* Streaming AI Responses
* Multi-PDF Knowledge Base
* Conversation Export

---

## 👨‍💻 Author

**Gaurav Aawanke**

Python Developer | AI Engineer | FastAPI | React | Generative AI | RAG

If you like this project, consider giving it a ⭐ on GitHub.
