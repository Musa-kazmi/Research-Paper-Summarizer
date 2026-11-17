<div align="center">

# 📚 ScholarAI: AI Research Paper Tool & Assistant

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.14-blue.svg)](https://www.python.org/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-v0.3+-green.svg)](https://www.langchain.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-2.5--Flash-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Summarize complex research papers, customize explanation styles, and engage in context-aware interactive discussions powered by Google Gemini and LangChain.**

[Live Demo](https://YOUR_STREAMLIT_APP_URL_HERE) • [Key Features](#-2-key-features) • [Quick Start](#-7-quick-start-guide) • [Deployment](#-8-deployment-guide)

</div>

---

## 📖 1. About & Project Overview

Navigating dense academic literature, mathematical formulations, and complex algorithmic architectures is time-consuming for researchers, students, and engineers alike. **ScholarAI** bridges this gap by combining **Streamlit**, **LangChain**, and **Google Gemini (`gemini-2.5-flash`)** into an intelligent research companion.

The application allows users to either select foundational machine learning papers or upload custom PDF documents. It extracts and analyzes the text, generates tailored summaries (ranging from intuitive analogies to rigorous mathematical code snippets), and passes the paper's synthesized context into an interactive conversational agent for deep follow-up discussions.

---

## ✨ 2. Key Features

| Feature | Description |
| :--- | :--- |
| **📄 Dual Input Modes** | Select foundational papers (*Attention Is All You Need*, *BERT*, *GPT-3*, *Diffusion Models*) or upload custom PDF documents. |
| **🎯 Tailored Explanation Styles** | Choose between **Beginner-Friendly**, **Technical**, **Code-Oriented**, and **Mathematical** explanations. |
| **📏 Flexible Length Control** | Generate summaries in **Short (1–2 paragraphs)**, **Medium (3–5 paragraphs)**, or **Long (detailed breakdown)** lengths. |
| **📐 Math & Intuitive Code** | Extracts formulas, translates abstract math into readable Python code snippets, and provides relatable analogies. |
| **💬 Context-Aware Chatbot** | Automatically transfers generated summary context to Tab 2 for continuous, multi-turn Q&A. |
| **🔒 Enterprise Key Management** | Seamlessly supports `.env`, **Streamlit Cloud Secrets**, and an in-app sidebar key input fallback. |

---

## 🛠️ 3. Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core application language (compatible with 3.10 – 3.14) |
| **Streamlit** | Interactive front-end user interface and multi-tab layout |
| **LangChain** (`langchain-google-genai`, `langchain-core`) | Prompt templating, model abstraction, and chain execution |
| **Google Gemini API** (`gemini-2.5-flash`) | State-of-the-art multimodal reasoning via the new `google-genai` SDK |
| **PyPDF (`pypdf`)** | High-performance PDF document text parsing and extraction |
| **Python-Dotenv** | Secure environment variable handling for local development |

---

## 🧠 4. Architecture & Workflow Pipeline

The application connects the user interface to Google Gemini through a clean LangChain pipeline:

```
[ Research Paper (PDF Upload or Predefined Selection) ]
                       │
                       ▼
       [ PyPDF Text Ingestion & Extraction ]
                       │
                       ▼
    [ LangChain PromptTemplate & Formatters ]
    (Explanation Style + Length + Math/Analogy Constraints)
                       │
                       ▼
    [ Google Gemini 2.5 Flash via google-genai ]
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
 [ Markdown Summary ]     [ Session State History ]
  (Rendered on Tab 1)      (Injected into Tab 2 Chatbot)
                                    │
                                    ▼
                         [ Interactive Q&A Assistant ]
```

| Pipeline Component | Implementation Details |
| :--- | :--- |
| **Document Ingestion** | Extracts text from uploaded PDFs using `pypdf.PdfReader` with intelligent prompt windowing (first 10,000 characters). |
| **Prompt Engineering** | Dynamic `PromptTemplate` strictly aligning summary outputs with target tone, math depth, and code analogies. |
| **Context Bridge** | Summary outputs automatically inject system notes into `st.session_state.chat_history` for persistent memory. |
| **Security Layer** | Multi-tier credential resolution: Environment variable -> Streamlit Cloud Secrets -> Sidebar interactive input. |

---

## 📈 5. Core Capabilities Explained

- **Multi-Level Persona Adaptation**: Seamlessly shifts explanatory depth from intuitive high-level metaphors (for students) to tensor-level matrix operations and pseudo-code (for engineers).
- **Hallucination Safeguards**: Structured prompt constraints instruct the model to declare *"Insufficient information available"* rather than guessing unverified claims.
- **Persistent Conversational Memory**: The chatbot retains context of the paper you just summarized, letting you ask for deeper mathematical proofs, real-world applications, or counter-arguments without re-pasting text.
- **Zero-Crash Cloud Fallback**: Automatically prevents Streamlit Cloud `ValidationError` crashes if API keys are not yet configured, guiding users gracefully via the sidebar.

---

## 🗂️ 6. Project Structure

```directory
ai-research-paper-assistant/
├── .env.example         # Template for environment variables (GEMINI_API_KEY)
├── .gitignore           # Prevents secrets, cache, and virtual envs from uploading
├── README.md            # Comprehensive documentation and project guide
├── requirements.txt     # Python dependencies for local run and cloud deployment
└── Research_agent.py    # Main Streamlit application with LangChain pipeline
```

---

## 🚀 7. Quick Start Guide

### Prerequisites
- Python 3.10 – 3.12 (or Python 3.14)
- A Gemini API Key from [Google AI Studio](https://aistudio.google.com/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-research-paper-assistant.git
   cd ai-research-paper-assistant
   ```

2. **Create a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API Key:**
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   Open `.env` and insert your Gemini API Key:
   ```env
   GEMINI_API_KEY="your_actual_api_key_here"
   ```

### How to Run Locally

Launch the Streamlit dashboard:
```bash
streamlit run Research_agent.py
```
Open **[http://localhost:8501](http://localhost:8501)** in your web browser.

---

## ☁️ 8. Deployment Guide

### Streamlit Community Cloud (Recommended)

1. Push your repository to GitHub.
2. Sign in to [share.streamlit.io](https://share.streamlit.io/) with your GitHub account.
3. Click **New app**, select your repository, branch (`main`), and set the main file path to:
   ```text
   Research_agent.py
   ```
4. **Configure Secrets (Crucial):**
   - Click **Advanced settings** (or **Manage app** -> **Settings** -> **Secrets** after deploy).
   - Add your API key in TOML format:
     ```toml
     GEMINI_API_KEY = "your_actual_api_key_here"
     ```
5. Click **Deploy!**

---

### Docker Deployment (Local / Cloud VM)

You can containerize the app using this `Dockerfile`:

```dockerfile
# Use official lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Launch application
ENTRYPOINT ["streamlit", "run", "Research_agent.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run the container:
```bash
docker build -t research-assistant .
docker run -p 8501:8501 -e GEMINI_API_KEY="your_api_key" research-assistant
```

---

## 👤 9. Author

- **Musa Kazmi**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [@your-profile](https://linkedin.com/in/your-profile)

---

## 📄 10. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
