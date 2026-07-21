from fastapi import FastAPI
from langgraph.types import Command
import uuid
from src.graph import graph
from src.graph import ReviewInput

app = FastAPI()


@app.post("/poll")
def poll():
    pending = []
    while True:
        thread_id = str(uuid.uuid4())
        config = {"configurable": {"thread_id": thread_id}}
        result = graph.invoke({}, config=config)
        if "__interrupt__" not in result:
            break
        payload = result["__interrupt__"][0].value
        pending.append(
            {
                "thread_id": thread_id,
                "video_title": payload.get("video_title"),
                "draft_reply": payload["draft_reply"],
                "comment_text": result.get("comment_text", ""),
            }
        )
    return {"pending": pending}


@app.post("/approve/{thread_id}")
def approve(thread_id: str, body: ReviewInput):
    config = {"configurable": {"thread_id": thread_id}}
    edited_reply = body.edited_reply
    graph.invoke(Command(resume=edited_reply), config=config)
    return {"status": "approved"}


@app.post("/reject/{thread_id}")
def reject(thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}
    graph.invoke(Command(resume=False), config=config)
    return {"status": "rejected"}
