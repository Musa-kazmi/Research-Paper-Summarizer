# 📚 AI Research Paper Tool & Assistant

An interactive AI-powered research assistant built with **Streamlit**, **LangChain**, and **Google Gemini (`gemini-2.5-flash`)**. 

This application allows you to summarize complex research papers (either from predefined seminal papers or by uploading custom PDF files), customize explanation styles and lengths, and interactively chat with an AI assistant that retains the context of the paper.

---

## ✨ Features

- 📄 **Dual Input Methods:**
  - **Predefined Papers:** Choose from foundational papers like *Attention Is All You Need*, *BERT*, *GPT-3*, and *Diffusion Models*.
  - **Custom PDF Upload:** Upload any research paper in `.pdf` format. Text is automatically parsed using `pypdf`.
- 🎯 **Customizable Explanation Styles:**
  - Beginner-Friendly
  - Technical
  - Code-Oriented
  - Mathematical (with intuitive equations and snippets)
- 📏 **Adjustable Length:**
  - Short (1–2 paragraphs)
  - Medium (3–5 paragraphs)
  - Long (detailed breakdown)
- 💬 **Context-Aware Interactive Chatbot:**
  - Automatically loads the generated paper summary into the chatbot's memory.
  - Ask follow-up questions, request deeper derivations, or clarify concepts.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Orchestration / LLM Framework:** [LangChain](https://www.langchain.com/) (`langchain-google-genai`, `langchain-core`)
- **LLM Provider:** [Google Gemini](https://ai.google.dev/) (`gemini-2.5-flash` via `google-genai` SDK)
- **PDF Extraction:** [PyPDF](https://pypdf.readthedocs.io/)
- **Configuration:** `python-dotenv`

---

## 🚀 Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key
1. Get a Gemini API Key from [Google AI Studio](https://aistudio.google.com/).
2. Copy the sample environment file:
   ```bash
   cp .env.example .env
   ```
3. Open `.env` and paste your key:
   ```env
   GEMINI_API_KEY="your_api_key_here"
   ```
   *(Or `GOOGLE_API_KEY="your_api_key_here"`)*

### 5. Run the Application
```bash
streamlit run Research_agent.py
```

The application will open in your default browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
├── Research_agent.py    # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env.example         # Template for environment variables
├── .gitignore           # Ignored files (protects secrets & artifacts)
└── README.md            # Project documentation
```

---

## 🔒 Security Note

Never commit your `.env` file or API keys to GitHub. The included `.gitignore` is pre-configured to keep your credentials safe.
