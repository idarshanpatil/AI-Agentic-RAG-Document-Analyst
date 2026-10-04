from src.rag_tool import search_documents
from src.tools import calculator
from src.rag_chain import generate_answer

def agent(question):

    question_lower = question.lower()

    # --------------------------------
    # Calculator detection
    # --------------------------------

    calculation_words = [
        "calculate",
        "multiply",
        "divide",
        "addition",
        "subtract"
    ]

    is_calculation = any(
        word in question_lower
        for word in calculation_words
    )

    # Only use calculator when the question
    # is actually a calculation
    if is_calculation and "what is" not in question_lower:

        expression = question_lower

        expression = expression.replace("calculate", "")
        expression = expression.replace("multiply", "*")
        expression = expression.replace("divide", "/")

        try:

            result = calculator(expression)

            return {
                "tool": "Calculator",
                "answer": result,
                "sources": []
            }

        except Exception:

            pass

    # --------------------------------
    # RAG Tool
    # --------------------------------

    documents = search_documents(question)

    context = "\n\n".join(
        doc["content"]
        for doc in documents
    )

    answer = generate_answer(
        question,
        context
    )

    return {
        "tool": "Document Search + LLM",
        "answer": answer,
        "sources": documents
    }


if __name__ == "__main__":

    question = input("\nAsk the AI Agent: ")

    result = agent(question)

    print("\n==============================")
    print("TOOL USED")
    print("==============================")

    print(result["tool"])

    print("\n==============================")
    print("ANSWER")
    print("==============================")

    print(result["answer"])

    print("\n==============================")
    print("SOURCES")
    print("==============================")

    for source in result["sources"]:

        print(
            f"{source['source']} | "
            f"Page: {source['page']}"
        )