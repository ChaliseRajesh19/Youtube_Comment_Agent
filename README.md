# 🤖 YouTube Comment Agent

An AI-powered YouTube comment moderation agent that automatically monitors your YouTube channel, generates contextual replies using an LLM, and lets you **approve, edit, or reject** every response before it is posted.

Built with **LangGraph**, **FastAPI**, **Streamlit**, and **Supabase**, the application provides persistent memory, human-in-the-loop review, and configurable AI behavior.

---

## ✨ Features

- 🎥 **Automatic Comment Discovery**
  - Scans your YouTube channel for new comments.
  - No need to manually enter video IDs.

- 🤖 **AI-Generated Replies**
  - Generates contextual replies using a Groq-hosted LLM.

- 👨‍💻 **Human-in-the-Loop Review**
  - Every generated reply pauses for review.
  - Nothing is posted automatically.

- ✏️ **Edit Draft Replies**
  - Modify AI-generated replies before posting.

- ✅ **Approve or Reject**
  - Approve to publish immediately.
  - Reject to discard the reply.

- ⚙️ **Configurable AI Settings**
  - Update the system prompt directly from the UI.
  - Customize the assistant's tone and behavior without changing code.

- 🧠 **Long-Term Memory**
  - Keeps track of processed comments.
  - Prevents duplicate replies even after application restarts.

- 💾 **Persistent Execution State**
  - LangGraph Checkpointer resumes interrupted workflows after restarts.

- 🌐 **Interactive Dashboard**
  - Built with Streamlit for reviewing comments and managing replies.

---

# 🏗️ Architecture

```text
                 Streamlit Community Cloud
                         │
                         ▼
                 Streamlit Dashboard
                         │
                         ▼
                  FastAPI Backend
                         │
                  LangGraph Agent
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
 YouTube Data API     Groq LLM      Supabase PostgreSQL
      (OAuth2)                      ├── PostgresSaver
                                    └── PostgresStore
```

---

# 🔄 Agent Workflow

```text
Check for New Comments
            │
            ▼
Retrieve Unhandled Comments
            │
            ▼
Generate AI Reply
            │
            ▼
Pause for Human Review
            │
      ┌─────┼──────────┐
      │     │          │
      ▼     ▼          ▼
 Approve  Edit      Reject
      │     │          │
      │     ▼          │
      │ Approve        │
      ▼                ▼
Post Reply      Mark as Handled
      │
      ▼
Store in Long-Term Memory
```

---

# 🛠️ Tech Stack

### AI & Agent

- LangGraph
- LangChain
- Groq (`openai/gpt-oss-20b`)

### Backend

- FastAPI

### Frontend

- Streamlit

### Database

- Supabase PostgreSQL
- LangGraph PostgresSaver
- LangGraph PostgresStore

### APIs

- YouTube Data API v3
- Google OAuth 2.0

### Deployment

- Docker
- Render (Backend)
- Streamlit Community Cloud (Frontend)

---

# 📁 Project Structure

```text
youtube-comment-agent/
│
├── src/
│   ├── graph.py
│   ├── nodes.py
│   ├── state.py
│   ├── youtube_client.py
│   ├── llm_utils.py
│   ├── memory.py
│   ├── checkpointer.py
│   └── settings.py
│
├── ui/
│   └── app.py
│
├── api.py
├── client.py
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

---

# 🚀 Setup

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-comment-agent.git

cd youtube-comment-agent
```

---

## 2. Enable YouTube Data API

1. Create a project in Google Cloud Console.
2. Enable **YouTube Data API v3**.
3. Configure the OAuth Consent Screen.
4. Create OAuth Desktop Credentials.
5. Authenticate once locally to obtain a Refresh Token.

---

## 3. Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=

DATABASE_URL=

GOOGLE_CLIENT_ID=

GOOGLE_CLIENT_SECRET=

GOOGLE_REFRESH_TOKEN=
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run the Backend

```bash
uvicorn api:app --reload
```

---

## 6. Run the Frontend

```bash
streamlit run ui/app.py
```

---

# 📋 How It Works

1. Click **Check for New Comments**.
2. The agent scans all uploaded videos.
3. New comments are discovered.
4. The LLM generates a contextual reply.
5. The workflow pauses for review.
6. You can:
   - ✅ Approve
   - ✏️ Edit & Approve
   - ❌ Reject
7. Processed comments are stored in long-term memory.
8. The same comment is never processed twice.

---

# ⚙️ Settings

The application includes a Settings page where you can configure the AI without modifying the source code.

Available options include:

- System Prompt
- Assistant Tone
- Reply Style
- Custom Instructions

Changes are applied immediately to future reply generations.

---

# 💾 Memory

The application uses LangGraph's persistent storage.

### Checkpointer

Stores the execution state so interrupted approval workflows can resume after server restarts.

### Long-Term Memory

Stores processed comment IDs to ensure comments are never replied to twice.

---

# 🌍 Deployment

| Component | Platform |
|-----------|----------|
| Frontend | Streamlit Community Cloud |
| Backend | Render |
| Database | Supabase PostgreSQL |
| Containerization | Docker |

---

# 🔮 Future Improvements

- Spam detection
- Pagination for large channels
- Background polling
- Async processing
- Multiple YouTube accounts
- Confidence-based automatic replies
- Reply analytics dashboard

---

# 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Rajesh Chalise**

- GitHub: https://github.com/ChaliseRajesh19
- Portfolio: https://chaliserajesh.com.np