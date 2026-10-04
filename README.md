# Customer Support AI Chatbot

A beginner-friendly customer support chatbot built with Python, LangChain, Google Gemini, and Streamlit.

## Features

- Interactive Streamlit chat interface
- Google Gemini LLM
- LangChain prompt template
- Conversation history
- Customer support style responses
- Secure API key handling with `.env`

## Tech Stack

- Python
- LangChain
- Google Gemini
- Streamlit
- python-dotenv

## Project Structure

```text
customer-support-chatbot/
├── app.py
├── chatbot.py
├── prompts.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

### 1. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API key

Create a `.env` file in the project folder:

```env
GOOGLE_API_KEY=your_api_key_here
```

Do not upload `.env` to GitHub.

### 4. Run the application

```bash
streamlit run app.py
```

## Example Questions

- Hello
- What payment methods do you support?
- How can I track my order?
- How do refunds work?
- I need help with my order.

## Architecture

```text
User
  ↓
Streamlit Chat UI
  ↓
LangChain Prompt Template
  ↓
Conversation History
  ↓
Google Gemini
  ↓
Response
  ↓
User
```

## Future Improvements

- Add a company FAQ knowledge base
- Add RAG with ChromaDB
- Add PDF document upload
- Add source citations
- Add persistent chat history
- Add authentication
