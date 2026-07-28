import streamlit as st
from client import get_comments, approve_comment, reject_comment

DEMO_VIDEO_URL = "https://youtu.be/R22sAI1JNw8"

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Comment Console",
    page_icon="◉",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# DESIGN SYSTEM
# ============================================================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root{
    --bg:#0B0D10;
    --panel:#14171C;
    --panel-alt:#191D24;
    --border:#262B33;
    --amber:#F2A93C;
    --amber-dim:rgba(242,169,60,0.12);
    --green:#3FBF7F;
    --green-dim:rgba(63,191,127,0.10);
    --red:#F0554B;
    --red-dim:rgba(240,85,75,0.10);
    --text:#E7E9EC;
    --text-dim:#8B93A1;
}

.main{ background-color:var(--bg); }
.block-container{ padding-top:1.2rem; padding-bottom:2.5rem; max-width:1000px; }

h1,h2,h3,h4{ font-family:'Space Grotesk',sans-serif !important; color:var(--text) !important; letter-spacing:-0.01em; }
p,span,div,label{ font-family:'Inter',sans-serif; }
.mono{ font-family:'JetBrains Mono',monospace !important; }

/* ---- console header ---- */
.console-bar{
    display:flex; align-items:center; justify-content:space-between;
    background:var(--panel); border:1px solid var(--border); border-radius:12px;
    padding:14px 20px; margin-bottom:22px;
}
.signal{ display:flex; align-items:center; gap:10px; }
.dot{
    width:9px; height:9px; border-radius:50%; background:var(--amber);
    box-shadow:0 0 0 0 rgba(242,169,60,0.6);
    animation:pulse 2s infinite;
}
@keyframes pulse{
    0%{ box-shadow:0 0 0 0 rgba(242,169,60,0.5); }
    70%{ box-shadow:0 0 0 8px rgba(242,169,60,0); }
    100%{ box-shadow:0 0 0 0 rgba(242,169,60,0); }
}
.signal-text{ font-family:'JetBrains Mono',monospace; font-size:0.78rem; color:var(--amber); letter-spacing:0.08em; }
.stack-tags{ display:flex; gap:6px; flex-wrap:wrap; }
.tag{
    font-family:'JetBrains Mono',monospace; font-size:0.68rem; color:var(--text-dim);
    background:var(--panel-alt); border:1px solid var(--border); border-radius:6px;
    padding:3px 8px;
}

/* ---- hero ---- */
.eyebrow{
    font-family:'JetBrains Mono',monospace; font-size:0.75rem; color:var(--amber);
    letter-spacing:0.12em; text-transform:uppercase; margin-bottom:6px;
}
.hero-sub{ color:var(--text-dim); font-size:1rem; max-width:640px; line-height:1.55; }

/* ---- monitor frame for the demo video ---- */
.monitor-frame{
    background:var(--panel); border:1px solid var(--border); border-radius:14px;
    padding:10px; margin:18px 0 6px 0;
}
.monitor-label{
    font-family:'JetBrains Mono',monospace; font-size:0.72rem; color:var(--text-dim);
    padding:4px 6px 10px 6px; display:flex; justify-content:space-between;
}

/* ---- gauge cards ---- */
.gauge{
    background:var(--panel); border:1px solid var(--border); border-radius:12px;
    padding:16px 18px;
}
.gauge-label{ font-family:'JetBrains Mono',monospace; font-size:0.72rem; color:var(--text-dim); letter-spacing:0.06em; text-transform:uppercase; }
.gauge-value{ font-family:'Space Grotesk',sans-serif; font-size:2rem; font-weight:600; color:var(--text); }

/* ---- ticket cards ---- */
.ticket{
    background:var(--panel); border:1px solid var(--border); border-radius:12px;
    padding:20px; margin-bottom:16px;
}
.ticket-head{ display:flex; align-items:center; gap:10px; margin-bottom:12px; }
.ticket-id{
    font-family:'JetBrains Mono',monospace; font-size:0.7rem; color:var(--amber);
    background:var(--amber-dim); border:1px solid rgba(242,169,60,0.3);
    border-radius:6px; padding:2px 8px;
}
.ticket-video{ font-family:'Space Grotesk',sans-serif; font-weight:600; color:var(--text); font-size:1rem; }

.field-label{ font-family:'JetBrains Mono',monospace; font-size:0.68rem; color:var(--text-dim); letter-spacing:0.06em; text-transform:uppercase; margin-bottom:4px; }
.comment-box{
    background:var(--panel-alt); border-left:2px solid var(--border);
    padding:10px 14px; border-radius:8px; margin-bottom:14px; font-size:0.92rem; color:var(--text-dim);
}
.draft-box{
    background:var(--green-dim); border-left:2px solid var(--green);
    padding:10px 14px; border-radius:8px; margin-bottom:14px; font-size:0.92rem; color:var(--text);
}

.stButton>button{
    width:100%; border-radius:8px; height:42px; font-weight:600;
    font-family:'Inter',sans-serif; border:1px solid var(--border);
}

.footer{ text-align:center; color:var(--text-dim); font-family:'JetBrains Mono',monospace; font-size:0.72rem; margin-top:36px; }
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# SESSION STATE
# ============================================================

if "pending_items" not in st.session_state:
    st.session_state.pending_items = []
if "approved_count" not in st.session_state:
    st.session_state.approved_count = 0
if "rejected_count" not in st.session_state:
    st.session_state.rejected_count = 0

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("### ◉ Comment Console")
    st.caption("Agent status: **ready**")
    st.divider()
    st.markdown("**Capabilities**")
    for f in [
        "Automatic comment discovery",
        "AI reply generation",
        "Human approval — edit or reject",
        "Persistent long-term memory",
        "LangGraph workflow",
    ]:
        st.markdown(f"— {f}")
    st.divider()
    st.markdown("**Stack**")
    st.code("LangGraph · FastAPI\nPostgreSQL · Groq\nStreamlit · Docker", language=None)

# ============================================================
# CONSOLE HEADER
# ============================================================

st.markdown(
    """
<div class="console-bar">
    <div class="signal">
        <div class="dot"></div>
        <span class="signal-text">LIVE — MONITORING CHANNEL</span>
    </div>
    <div class="stack-tags">
        <span class="tag">langgraph</span>
        <span class="tag">postgres</span>
        <span class="tag">groq</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# HERO
# ============================================================

st.markdown('<div class="eyebrow">Agent Console</div>', unsafe_allow_html=True)
st.markdown("## Comment Response Queue")
st.markdown(
    '<div class="hero-sub">Every new comment on your channel gets a drafted reply here first. '
    "Nothing posts without your sign-off — approve as-is, edit it, or reject it.</div>",
    unsafe_allow_html=True,
)

# ============================================================
# DEMO — video embedded directly, watch + comment inline
# ============================================================

st.markdown(
    """
<div class="monitor-frame">
    <div class="monitor-label"><span>DEMO FEED</span><span>comment below, then check for new activity</span></div>
</div>
""",
    unsafe_allow_html=True,
)
st.video(DEMO_VIDEO_URL)

st.write("")

# ============================================================
# DASHBOARD — gauges
# ============================================================

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        f'<div class="gauge"><div class="gauge-label">Pending</div><div class="gauge-value">{len(st.session_state.pending_items)}</div></div>',
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        f'<div class="gauge"><div class="gauge-label">Approved</div><div class="gauge-value">{st.session_state.approved_count}</div></div>',
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        f'<div class="gauge"><div class="gauge-label">Rejected</div><div class="gauge-value">{st.session_state.rejected_count}</div></div>',
        unsafe_allow_html=True,
    )

st.write("")

if st.button("↻  Check new comments", use_container_width=True):
    with st.spinner("Scanning channel for new activity..."):
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
    if st.session_state.pending_items:
        st.success(
            f"{len(st.session_state.pending_items)} new comment(s) queued for review."
        )
    else:
        st.info("Channel is clear — no new comments.")

st.divider()

# ============================================================
# REVIEW QUEUE — ticket cards
# ============================================================

st.markdown("### Review Queue")

if st.session_state.pending_items:
    for i, item in enumerate(st.session_state.pending_items):
        editing_key = f"editing_{item['thread_id']}"
        if editing_key not in st.session_state:
            st.session_state[editing_key] = False

        ticket_id = f"REPLY-{i+1:03d}"

        st.markdown('<div class="ticket">', unsafe_allow_html=True)
        st.markdown(
            f'<div class="ticket-head"><span class="ticket-id mono">{ticket_id}</span>'
            f'<span class="ticket-video">{item["video_title"]}</span></div>',
            unsafe_allow_html=True,
        )

        st.markdown('<div class="field-label">Comment</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="comment-box">{item["comment_text"]}</div>',
            unsafe_allow_html=True,
        )

        if not st.session_state[editing_key]:
            st.markdown(
                '<div class="field-label">Draft reply</div>', unsafe_allow_html=True
            )
            st.markdown(
                f'<div class="draft-box">{item["draft_reply"]}</div>',
                unsafe_allow_html=True,
            )

            b1, b2, b3 = st.columns(3)
            if b1.button("Approve", key=f"approve_{item['thread_id']}"):
                if approve_comment(item["thread_id"], item["draft_reply"]):
                    st.session_state.approved_count += 1
                    st.session_state.pending_items.pop(i)
                st.rerun()
            if b2.button("Change", key=f"change_{item['thread_id']}"):
                st.session_state[editing_key] = True
                st.rerun()
            if b3.button("Reject", key=f"reject_{item['thread_id']}"):
                if reject_comment(item["thread_id"]):
                    st.session_state.rejected_count += 1
                    st.session_state.pending_items.pop(i)
                st.rerun()
        else:
            st.markdown(
                '<div class="field-label">Edit reply</div>', unsafe_allow_html=True
            )
            edited = st.text_area(
                "Edit reply",
                value=item["draft_reply"],
                key=f"edit_{item['thread_id']}",
                label_visibility="collapsed",
            )
            b1, b2 = st.columns(2)
            if b1.button("Save & approve", key=f"save_{item['thread_id']}"):
                if approve_comment(item["thread_id"], edited):
                    st.session_state.approved_count += 1
                    st.session_state.pending_items.pop(i)
                st.rerun()
            if b2.button("Cancel", key=f"cancel_{item['thread_id']}"):
                st.session_state[editing_key] = False
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown(
        '<div class="ticket" style="text-align:center; color:var(--text-dim);">'
        "Queue is empty. Run a check above to pull in new comments.</div>",
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="footer">COMMENT-CONSOLE · LANGGRAPH + FASTAPI + POSTGRES</div>',
    unsafe_allow_html=True,
)
