from typing import TypedDict


class AgentState(TypedDict):
    """
    Represents the state of an agent in the system.
    """

    video_id: str
    video_title: str
    comment_id: str
    comment_text: str
    draft_reply: str
    approved: bool

