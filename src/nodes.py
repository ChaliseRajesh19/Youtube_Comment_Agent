from src.youtube_client import (
    get_new_comments,
    reply_to_comment,
    get_channel_videos,
    get_uploads_playlist_id,
)
from src.state import AgentState
from src.llm_utils import call_llm, make_system_prompt
from src.memory import get_postgres_store

namespace = ("replied_comments",)

store = get_postgres_store()

# Replace with your channel's uploads playlist ID


def fetch_comment_node(state: AgentState):
    playlist_id = get_uploads_playlist_id()
    videos = get_channel_videos(playlist_id)
    for video_id, video_title in videos:
        comments = get_new_comments(video_id)
        for comment_id, comment_txt in comments:
            if store.get(namespace, comment_id) is None:
                store.put(
                    namespace, comment_id, {"status": "pending"}
                )  # ← mark immediately
                return {
                    "comment_id": comment_id,
                    "comment_text": comment_txt,
                    "video_title": video_title,
                }
    return {"comment_id": None, "comment_text": None, "video_title": None}


def draft_reply_node(state: AgentState):
    comment_text = state["comment_text"]

    prompt_response = make_system_prompt(comment_text)

    llm = call_llm()
    response = llm.invoke(prompt_response)

    return {"draft_reply": response.content}


def post_reply_node(state: AgentState):
    if not state.get("approved"):
        store.put(namespace, state["comment_id"], {"status": "rejected"})
        return {"approved": False}
    reply_to_comment(state["comment_id"], state["draft_reply"])
    store.put(namespace, state["comment_id"], {"status": "replied"})
    return {"approved": True}

