\# 🤖 AI-Powered Agentic RAG Document Analyst



An AI-powered Agentic RAG application that allows users to ask questions about PDF documents, retrieve relevant information using semantic search, generate grounded answers using an open-source LLM, and perform calculations using an integrated calculator tool.



\## 🚀 Features



\- PDF document processing

\- Automatic text extraction

\- Recursive text chunking

\- Hugging Face sentence embeddings

\- FAISS vector database

\- Semantic document retrieval

\- Retrieval-Augmented Generation (RAG)

\- FLAN-T5 language model

\- AI Agent routing

\- Document Search Tool

\- Calculator Tool

\- Source/page references

\- Streamlit chat interface

\- Conversation history



\## 🏗️ Architecture



User

↓

Streamlit UI

↓

AI Agent

↓

Tool Selection

├── Document Search Tool

│   ↓

│   FAISS Vector Database

│   ↓

│   Relevant PDF Chunks

│   ↓

│   FLAN-T5

│

└── Calculator Tool

↓

Result



\## 🛠️ Technologies



\- Python

\- Streamlit

\- LangChain

\- Hugging Face Transformers

\- Sentence Transformers

\- FAISS

\- PyPDF

\- PyTorch



\## 📂 Project Structure



AI\_Agentic\_RAG/

│

├── app.py

├── README.md

│

├── src/

│   ├── agent.py

│   ├── rag\_tool.py

│   ├── tools.py

│   ├── rag\_chain.py

│   ├── retriever.py

│   ├── document\_loader.py

│   ├── text\_splitter.py

│   └── vector\_store.py

│

├── data/

│   └── documents/

│

└── vector\_db/



\## ⚙️ Installation



Create and activate the Conda environment:



```bash

conda create -n agentic\_rag python=3.11

conda activate agentic\_rag

Install dependencies:



pip install streamlit

pip install langchain

pip install langchain-community

pip install langchain-huggingface

pip install langchain-text-splitters

pip install faiss-cpu

pip install pypdf

pip install sentence-transformers

pip install transformers

pip install torch

▶️ Run the Application



From the project directory:



python -m streamlit run app.py



The application will open in the browser.



💬 Example Questions

Document Question

What is pooling?



The system retrieves relevant content from the PDF and generates an answer.



Calculator

calculate 25 \* 40



The Agent routes the query to the calculator tool.



🧠 How RAG Works

PDF documents are loaded.

Text is extracted from the documents.

Text is divided into smaller chunks.

Each chunk is converted into an embedding.

Embeddings are stored in FAISS.

User questions are converted into embeddings.

Relevant document chunks are retrieved.

Retrieved context is provided to FLAN-T5.

The model generates an answer using the retrieved information.

🤖 Agentic Workflow



The Agent analyzes the user query and selects the appropriate tool.



For document-related questions:



Question

↓

Document Search Tool

↓

FAISS Retriever

↓

Relevant Context

↓

FLAN-T5

↓

Answer



For calculations:



Question

↓

Calculator Tool

↓

Result

📌 Project Highlights

Built a complete Retrieval-Augmented Generation pipeline.

Implemented semantic search using FAISS.

Integrated Hugging Face embeddings and FLAN-T5.

Developed an Agent-based tool routing system.

Added calculator and document search tools.

Built an interactive Streamlit chat interface.

Implemented source-aware document responses.

🔮 Future Improvements

Multi-agent architecture

Better conversational memory

Support for DOCX and TXT files

Improved LLM models

Hybrid search

Reranking

Authentication

Cloud deployment

