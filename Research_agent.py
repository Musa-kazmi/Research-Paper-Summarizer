import os
import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# 1. Load Environment Variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

# 2. Initialize Gemini Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
)

# Page Configuration
st.set_page_config(page_title="Research Tool & Assistant", layout="wide")
st.title("📚 AI Research Paper Tool & Assistant")

# Initialize Session States for Chat & Active Context
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "active_paper_context" not in st.session_state:
    st.session_state.active_paper_context = None

# Create tabs
tab1, tab2 = st.tabs(["📄 Paper Summarizer & Upload", "💬 Interactive Chatbot"])


with tab1:
    st.header("Research Paper Summarizer")

    # Selection mode: Pick predefined OR upload custom PDF
    input_method = st.radio("Choose Input Method:", ["Select Predefined Paper", "Upload PDF File"])

    paper_name = ""
    paper_text_content = ""

    if input_method == "Select Predefined Paper":
        paper_name = st.selectbox(
            "Select Research Paper Name",
            [
                "Attention Is All You Need",
                "BERT: Pre-training of Deep Bidirectional Transformers",
                "GPT-3: Language Models are Few-Shot Learners",
                "Diffusion Models Beat GANs on Image Synthesis",
            ],
        )
    else:
        uploaded_file = st.file_uploader("Upload a Research Paper PDF", type=["pdf"])
        if uploaded_file is not None:
            paper_name = uploaded_file.name
            # Extract text from uploaded PDF
            pdf_reader = PdfReader(uploaded_file)
            paper_text_content = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
            st.success(f"Successfully uploaded: **{paper_name}** ({len(pdf_reader.pages)} pages)")

    style_input = st.selectbox(
        "Select Explanation Style",
        ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
    )

    length_input = st.selectbox(
        "Select Explanation Length",
        ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"],
    )

    template = PromptTemplate(
        template="""Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}

Paper Content Context (if available):
{paper_content}

1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
   - Use relatable analogies to simplify complex ideas.
Note: If Paper Content Context is "N/A", use your pre-trained knowledge base to summarize this paper. If specific information is unavailable in the paper or knowledge base, state "Insufficient information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.""",
        input_variables=["paper_input", "style_input", "length_input", "paper_content"],
    )

    if st.button("Summarize"):
        if paper_name:
            with st.spinner("Generating summary..."):
                chain = template | model
                
                # Pass first 10,000 characters of uploaded PDF to fit prompt limit if uploaded
                content_snippet = paper_text_content[:10000] if paper_text_content else "N/A"
                
                response = chain.invoke({
                    "paper_input": paper_name,
                    "style_input": style_input,
                    "length_input": length_input,
                    "paper_content": content_snippet
                })

                st.markdown(response.content)

                # Store active context in session state
                st.session_state.active_paper_context = {
                    "paper_name": paper_name,
                    "summary": response.content
                }

                # Automatically pass the summary context into Chatbot Memory
                context_message = (
                    f"System Note: The user generated a summary for the paper '{paper_name}'. "
                    f"Here is the summary generated:\n{response.content}\n"
                    f"Use this context to answer future user questions regarding this paper."
                )
                
                st.session_state.chat_history.append({"role": "user", "content": context_message})
                st.session_state.chat_history.append({
                    "role": "assistant", 
                    "content": f"I have received the summary context for **'{paper_name}'**. You can now switch to the Chatbot tab to ask me questions about it!"
                })

                st.info("💡 Summary sent to Chatbot! Switch to the 'Interactive Chatbot' tab to ask questions about this paper.")
        else:
            st.warning("Please select or upload a research paper first.")


with tab2:
    st.header("Chat with Assistant")

    # Banner displaying current active paper context
    if st.session_state.active_paper_context:
        st.info(f"📄 **Current Active Context:** {st.session_state.active_paper_context['paper_name']}")
    else:
        st.caption("No paper summarized yet. Summarize a paper in Tab 1 or ask general AI questions here.")

    # Render prior messages (hide initial hidden system context prompt for clean UI)
    for message in st.session_state.chat_history:
        if not message["content"].startswith("System Note:"):
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Chat input box
    if user_input := st.chat_input("Ask a follow-up question about the paper..."):
        # Display user question
        with st.chat_message("user"):
            st.markdown(user_input)

        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Generate response using entire context history
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = model.invoke(st.session_state.chat_history)
                st.markdown(response.content)

        st.session_state.chat_history.append({"role": "assistant", "content": response.content})