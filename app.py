import streamlit as st
from client import get_comments, approve_comment, reject_comment

st.title("YouTube Comment Agent")

if "pending_items" not in st.session_state:
    st.session_state.pending_items = []

if st.button("Check for new comments"):
    st.session_state.pending_items = []
    result = get_comments()
    for item in result.get("pending", []):
        st.session_state.pending_items.append(
            {
                "thread_id": item["thread_id"],
                "video_title": item["video_title"],
                "draft_reply": item["draft_reply"],
                "comment_text": item.get("comment_text", ""),
            }
        )

for i, item in enumerate(st.session_state.pending_items):
    st.subheader(item["video_title"])
    st.write(f"**Comment:** {item['comment_text']}")

    editing_key = f"editing_{i}"
    if editing_key not in st.session_state:
        st.session_state[editing_key] = False

    if not st.session_state[editing_key]:
        # Normal view — just show the draft
        st.write(f"**Draft reply:** {item['draft_reply']}")
        col1, col2, col3 = st.columns(3)
        if col1.button("✅ Approve", key=f"approve_{i}"):
            if approve_comment(item["thread_id"], item["draft_reply"]):
                st.session_state.pending_items.pop(i)
            st.rerun()
        if col2.button("✏️ Change", key=f"change_{i}"):
            st.session_state[editing_key] = True
            st.rerun()
        if col3.button("❌ Reject", key=f"reject_{i}"):
            if reject_comment(item["thread_id"]):
                st.session_state.pending_items.pop(i)
            st.rerun()
    else:
        # Editing view — text box appears only after clicking Change
        edited = st.text_area("Edit reply:", value=item["draft_reply"], key=f"edit_{i}")
        col1, col2 = st.columns(2)
        if col1.button("💾 Save & Approve", key=f"save_{i}"):
            if approve_comment(item["thread_id"], edited):
                st.session_state.pending_items.pop(i)
            st.rerun()
        if col2.button("Cancel", key=f"cancel_{i}"):
            st.session_state[editing_key] = False
            st.rerun()

    st.divider()
