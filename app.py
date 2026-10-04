import streamlit as st

from src.agent import agent


st.set_page_config(
    page_title="AI Agentic Document Analyst",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 AI Agentic Document Analyst")

st.write(
    "Ask questions about your documents or perform calculations "
    "using an AI Agent."
)


# -----------------------------------
# Initialize chat history
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------------
# Display previous messages
# -----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# -----------------------------------
# User input
# -----------------------------------

question = st.chat_input(
    "Ask the AI Agent..."
)


if question:

    # Show user message
    with st.chat_message("user"):

        st.write(question)


    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Agent is thinking..."):

            result = agent(question)

        st.write(result["answer"])


        # Tool information
        st.caption(
            f"🛠️ Tool Used: {result['tool']}"
        )


        # Sources
        if result["sources"]:

            st.subheader("📚 Sources")

            for i, source in enumerate(
                result["sources"],
                1
            ):

                st.markdown(
                    f"**Source {i}:** "
                    f"`{source['source']}` — "
                    f"Page `{source['page']}`"
                )


    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"]
        }
    )


# -----------------------------------
# Clear conversation
# -----------------------------------

if st.sidebar.button("🗑️ Clear Chat"):

    st.session_state.messages = []

    st.rerun()