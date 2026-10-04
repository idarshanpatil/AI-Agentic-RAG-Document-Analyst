from src.retriever import get_retriever


def search_documents(question):

    retriever = get_retriever()

    documents = retriever.invoke(question)

    results = []

    for doc in documents:

        results.append({
            "content": doc.page_content,
            "source": doc.metadata.get("source", "Unknown"),
            "page": doc.metadata.get("page", "Unknown")
        })

    return results


if __name__ == "__main__":

    question = input("Ask about your documents: ")

    results = search_documents(question)

    for i, result in enumerate(results, 1):

        print(f"\n--- Result {i} ---")
        print("Source:", result["source"])
        print("Page:", result["page"])
        print(result["content"][:500])