# 🤖 Q&A Chatbot with OpenAI + LangChain

A simple yet powerful Q&A chatbot built with **LangChain**, **OpenAI GPT models**, and **Streamlit**. Supports model selection, temperature control, and token limits — all from a clean sidebar UI.

---

## 🚀 Features

- **Multi-model support** — Choose between `gpt-4o`, `gpt-4-turbo`, and `gpt-4`
- **Adjustable parameters** — Control Temperature and Max Tokens via sliders
- **LangSmith tracing** — Full observability of LLM calls via LangChain tracing
- **Streamlit UI** — Lightweight, interactive web interface

---

## 🗂️ Project Structure

```
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not committed)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

> ⚠️ Never commit your `.env` file. It is already excluded via `.gitignore`.

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Enter your **OpenAI API key** in the sidebar
2. Select a **model** (`gpt-4o` recommended)
3. Adjust **Temperature** (creativity) and **Max Tokens** (response length)
4. Type your question in the input box and hit Enter

---

## 🧰 Tech Stack

| Tool | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Frontend UI |
| [LangChain](https://www.langchain.com/) | LLM orchestration |
| [OpenAI](https://platform.openai.com/) | Language models |
| [LangSmith](https://smith.langchain.com/) | Tracing & observability |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment management |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
