from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_documents(folder_path):
    documents = []

    folder = Path(folder_path)

    for pdf_file in folder.glob("*.pdf"):
        print(f"Loading: {pdf_file.name}")

        loader = PyPDFLoader(str(pdf_file))
        pdf_documents = loader.load()

        documents.extend(pdf_documents)

    return documents


if __name__ == "__main__":
    docs = load_documents("data/documents")

    print(f"\nTotal pages loaded: {len(docs)}")

    if docs:
        print("\nFirst page preview:")
        print(docs[0].page_content[:1000])