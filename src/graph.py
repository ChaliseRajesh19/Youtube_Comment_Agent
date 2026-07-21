from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt
from src.state import AgentState
from src.nodes import fetch_comment_node, draft_reply_node, post_reply_node
from src.checkpointer import get_postgres_checkpointer
from pydantic import BaseModel

checkpointer = get_postgres_checkpointer()


class ReviewInput(BaseModel):
    edited_reply: str | None = None


def should_continue(state: AgentState):
    if state.get("comment_id") is None:
        return "end"
    return "continue"


def review_node(state: AgentState):
    decision = interrupt(
        {
            "draft_reply": state["draft_reply"],
            "video_title": state["video_title"],
            "prompt": "Do you approve this reply? (True/False)",
        }
    )
    if decision:
        return {"draft_reply": decision, "approved": True}
    return {"approved": decision}


builder = StateGraph(AgentState)
builder.add_node("fetch_comment", fetch_comment_node)
builder.add_node("draft_reply", draft_reply_node)
builder.add_node("review", review_node)
builder.add_node("post_reply", post_reply_node)

builder.add_edge(START, "fetch_comment")
builder.add_conditional_edges(
    "fetch_comment", should_continue, {"continue": "draft_reply", "end": END}
)
builder.add_edge("draft_reply", "review")
builder.add_edge("review", "post_reply")
builder.add_edge("post_reply", END)

graph = builder.compile(checkpointer=checkpointer)
