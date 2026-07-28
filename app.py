import streamlit as st
from client import get_comments, approve_comment, reject_comment

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="YouTube Comment Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

.main{
    background-color:#0E1117;
}

.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
}

.hero{
    padding:25px;
    border-radius:18px;
    background:linear-gradient(135deg,#FF0000,#7B2FF7);
    color:white;
}

.metric-card{
    background:#1E1E1E;
    padding:18px;
    border-radius:15px;
    border:1px solid #2d2d2d;
}

.project-card{
    background:#161B22;
    padding:18px;
    border-radius:15px;
    border:1px solid #2b3137;
    margin-bottom:20px;
}

.try-card{
    background:#1B2430;
    padding:20px;
    border-radius:15px;
    border-left:6px solid #FF0000;
}

.stButton>button{
    width:100%;
    border-radius:10px;
    height:45px;
    font-weight:600;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}

</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# SESSION STATE
# ============================================================

if "pending_items" not in st.session_state:
    st.session_state.pending_items = []

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🤖 YouTube Comment Agent")

    st.success("AI Agent Ready")

    st.divider()

    st.subheader("Features")

    st.write("✅ Automatic Comment Discovery")
    st.write("✅ AI Reply Generation")
    st.write("✅ Human Approval")
    st.write("✅ Persistent Memory")
    st.write("✅ LangGraph Workflow")
    st.write("✅ FastAPI Backend")
    st.write("✅ PostgreSQL")
    st.write("✅ Docker Deployment")

    st.divider()

    st.info("""
**Tech Stack**

- LangGraph
- FastAPI
- PostgreSQL
- Groq
- Streamlit
- Docker
""")

# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
    """
<div class="hero">

# 🤖 YouTube Comment Agent

### AI-powered YouTube Comment Management

Automatically discover new YouTube comments, generate intelligent AI replies,
and approve or edit them before publishing.

Built using **LangGraph · FastAPI · PostgreSQL · Docker**

</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# ============================================================
# TRY DEMO SECTION
# ============================================================

st.markdown(
    """
<div class="try-card">

## 🎬 Try it Yourself

Want to see the AI Agent in action?

### Step 1
Open the demo YouTube video.

### Step 2
Leave any comment.

### Step 3
Come back here.

### Step 4
Click **Check New Comments**.

The AI will automatically discover your comment and generate a reply.

</div>
""",
    unsafe_allow_html=True,
)

st.link_button(
    "▶ Open Demo YouTube Video",
    "https://youtu.be/R22sAI1JNw8",
    use_container_width=True,
)

st.write("")

# ============================================================
# DASHBOARD
# ============================================================

st.subheader("📊 Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Pending", len(st.session_state.pending_items))
col2.metric("Approved", "--")
col3.metric("Rejected", "--")

st.write("")

# ============================================================
# CHECK COMMENTS BUTTON
# ============================================================

if st.button("🔄 Check New Comments"):

    with st.spinner("🤖 AI Agent is checking YouTube comments..."):

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

    st.success("Comments loaded successfully.")

st.divider()
