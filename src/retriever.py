from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


VECTOR_DB_PATH = "vector_db"


def get_retriever():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever


if __name__ == "__main__":

    retriever = get_retriever()

    question = input("Ask a question: ")

    documents = retriever.invoke(question)

    print("\nRetrieved Documents:\n")

    for i, doc in enumerate(documents, 1):

        print(f"--- Document {i} ---")
        print(doc.page_content[:500])
        print()