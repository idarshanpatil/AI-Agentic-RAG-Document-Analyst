from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from src.document_loader import load_documents
from src.text_splitter import split_documents


DOCUMENT_PATH = "data/documents"
VECTOR_DB_PATH = "vector_db"


def create_vector_store():

    print("Loading documents...")

    documents = load_documents(DOCUMENT_PATH)

    if not documents:
        print("No PDF documents found.")
        return

    print(f"Loaded {len(documents)} pages.")

    print("Splitting documents...")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating embeddings...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating FAISS vector database...")

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    Path(VECTOR_DB_PATH).mkdir(
        parents=True,
        exist_ok=True
    )

    vector_store.save_local(VECTOR_DB_PATH)

    print("Vector database created successfully!")
    print(f"Saved to: {VECTOR_DB_PATH}")


if __name__ == "__main__":
    create_vector_store()