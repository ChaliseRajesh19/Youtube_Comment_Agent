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
else:

    st.success("🎉 No Pending Comments")

    st.markdown("""
### Everything is up to date!

The AI Agent has processed all pending comments.

### Want to test it?

1. Click the **Open Demo YouTube Video** button above.
2. Leave any comment.
3. Return here.
4. Click **🔄 Check New Comments**.

The AI will automatically discover your comment and generate a reply.
""")

st.divider()

# ============================================================
# ABOUT PROJECT
# ============================================================

tab1, tab2, tab3 = st.tabs(
    [
        "🚀 About Project",
        "🏗 Architecture",
        "🛠 Tech Stack",
    ]
)

# ------------------------------------------------------------

with tab1:

    st.subheader("🤖 YouTube Comment Agent")

    st.write("""
This application automatically monitors YouTube comments,
uses an LLM to generate intelligent replies,
and allows creators to approve, edit,
or reject responses before publishing.

It demonstrates how modern AI Agents can automate repetitive
community management tasks while keeping humans in control.
""")

    st.write("### ✨ Features")

    col1, col2 = st.columns(2)

    with col1:

        st.success("Automatic Comment Discovery")
        st.success("AI Reply Generation")
        st.success("Human Approval Workflow")
        st.success("Persistent Memory")

    with col2:

        st.success("LangGraph Agent")
        st.success("FastAPI Backend")
        st.success("Docker Deployment")
        st.success("PostgreSQL Storage")

# ------------------------------------------------------------

with tab2:

    st.subheader("🏗 System Architecture")

    st.code("""
                 YouTube API
                      │
                      ▼
          Discover New Comments
                      │
                      ▼
             LangGraph Workflow
                      │
                      ▼
          Large Language Model
                      │
                      ▼
            AI Draft Generation
                      │
                      ▼
            Human Review (UI)
             ┌────────┴────────┐
             ▼                 ▼
         Approve            Reject
             │
             ▼
      Reply Posted to YouTube
""")

    st.info("""
This project follows a **Human-in-the-Loop Agent Workflow**
where AI drafts replies while the creator maintains full control
over what gets published.
""")

# ------------------------------------------------------------

with tab3:

    st.subheader("🛠 Technologies")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
### AI

- LangGraph
- Groq LLM
- Prompt Engineering
- AI Agents
""")

    with c2:

        st.markdown("""
### Backend

- FastAPI
- PostgreSQL
- YouTube Data API
- REST APIs
""")

    with c3:

        st.markdown("""
### DevOps

- Docker
- Streamlit
- GitHub
- Python
""")

st.divider()

# ============================================================
# CONTACT
# ============================================================

st.subheader("👨‍💻 Developer")

st.markdown("""
**Rajesh Chalise**

AI Engineer focused on building production-ready
LLM applications and Agentic AI systems.

- 🌐 Portfolio: https://www.chaliserajesh.com.np
- 💼 LinkedIn: https://linkedin.com/in/chaliserajesh19
- 📧 Email: chaliseinai@gmail.com
- 💻 GitHub: https://github.com/ChaliseRajesh19
""")

st.divider()

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">

### 🤖 YouTube Comment Agent

Built with ❤️ using

LangGraph • FastAPI • PostgreSQL • Docker • Streamlit

© 2026 Rajesh Chalise

</div>
""",
    unsafe_allow_html=True,
)
