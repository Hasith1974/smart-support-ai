import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import prompt


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is missing. "
        "Add it to your .env file."
    )


llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.2,
    google_api_key=GOOGLE_API_KEY,

    # Lower reasoning effort for faster customer support
    thinking_level="low"
)


chain = prompt | llm


def extract_text(content):

    if isinstance(content, str):
        return content

    if isinstance(content, list):

        text_parts = []

        for item in content:

            if isinstance(item, dict):

                if item.get("type") == "text":
                    text_parts.append(
                        item.get("text", "")
                    )

        return "".join(text_parts)

    return str(content)


def get_response_stream(question, chat_history):

    for chunk in chain.stream({
        "question": question,
        "chat_history": chat_history
    }):

        text = extract_text(chunk.content)

        if text:
            yield text