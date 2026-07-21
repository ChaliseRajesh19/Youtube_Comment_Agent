import os
from dotenv import load_dotenv

load_dotenv()
from langchain_groq import ChatGroq


def make_system_prompt(comment_text):
    return f"""You are replying to a comment on my YouTube video, as me (the channel owner).

Rules:
- Keep it short: 1-2 sentences, casual and friendly tone.
- Thank or acknowledge the commenter naturally, don't sound robotic or repeat "thank you for watching" every time.
- If it's a question, answer directly if you can, or say you'll cover it in a future video.
- If it's spam, an ad, or unrelated to the video, reply with exactly: "SKIP"
- Never make promises about specific dates, collabs, or giveaways.
- No emojis unless the comment itself uses them.
- Do not mention that you are an AI.

Comment: "{comment_text}"

Reply:"""


def call_llm():
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3,
    )
    return llm
