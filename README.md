# 🤖 Smart AI Assistant

A Full-Stack AI Assistant built with **React.js**, **FastAPI**, **PostgreSQL**, **ChromaDB**, and **Qwen LLM**.

The assistant supports multi-session conversations, memory management, AI tools, and Retrieval-Augmented Generation (RAG) using uploaded PDF documents.

---

## 🚀 Features

* 💬 AI Chat Assistant
* 📝 Multi-Session Chat History
* 🧠 Memory-Based Conversations
* 📄 PDF Upload
* 🔍 Retrieval-Augmented Generation (RAG)
* 📚 ChromaDB Vector Database
* 🌦️ Weather Tool
* 🔎 Search Tool
* 🧮 Calculator Tool
* ✈️ Travel Tool
* 💾 PostgreSQL Database
* ⚡ FastAPI Backend
* 🎨 React Frontend

---

## 🏗️ Project Architecture

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

---

## 🧠 RAG Workflow

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
Similarity Search
↓
Retrieve Relevant Chunks
↓
Context + Qwen
↓
Generate Answer

---

## 🛠️ Tech Stack

### Frontend

* React.js
* Tailwind CSS

### Backend

* Python
* FastAPI

### Database

* PostgreSQL
* ChromaDB

### AI & ML

* Qwen LLM
* LangChain
* Embedding Model

---

## 📂 Key Features

### Chat System

* Multi-session conversations
* Chat history
* Conversation persistence

### Memory System

* Stores user information
* Retrieves previous context
* Personalized conversations

### AI Tools

* Weather
* Search
* Calculator
* Travel

### RAG

* PDF Upload
* Embedding Generation
* Vector Search
* Context Retrieval
* AI-powered Answers

---

## 📌 Future Improvements

* Docker Support
* Project Deployment
* Authentication
* Streaming Responses
* Multiple Document Collections
* Conversation Export

---

## 👨‍💻 Author

**Gaurav Aawanke**

Python Developer | AI Engineer | FastAPI | React | Generative AI | RAG

---

⭐ If you found this project useful, consider giving it a star.
