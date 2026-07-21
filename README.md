# YouTube Comment Agent

An AI agent that monitors your YouTube channel for new comments, drafts replies using an LLM, and posts them only after your approval. Built with LangGraph, featuring persistent long-term memory and a human-in-the-loop approval flow.

## Features

- **Automatic comment discovery** — scans all videos on your channel for new comments (no manual video ID entry)
- **AI-drafted replies** — Groq-hosted LLM drafts a contextual reply to each comment
- **Human-in-the-loop approval** — every reply pauses for your review before posting; nothing goes out without explicit approval
- **Long-term memory** — tracks which comments have already been handled, so the agent never re-processes or double-replies to the same comment across restarts
- **Persistent execution state** — built on LangGraph's checkpointer, so an in-progress review survives a server restart
- **Web UI** — Streamlit dashboard to review pending drafts and approve/reject with one click

## Architecture

```
Streamlit UI  →  FastAPI backend  →  LangGraph agent
                                          │
                                          ├── YouTube Data API v3 (read/reply)
                                          ├── Groq LLM (draft generation)
                                          └── Supabase Postgres
                                                ├── Checkpointer (paused run state)
                                                └── Store (long-term memory / dedup)
```

**Agent flow:** discover new comment → draft reply → pause (`interrupt()`) for human review → on approval, post reply and mark as handled in memory.

## Tech Stack

- **Orchestration:** LangGraph (`StateGraph`, `interrupt()`, `PostgresSaver`, `PostgresStore`)
- **LLM:** Groq (`openai/gpt-oss-20b`)
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Database:** Supabase (Postgres)
- **APIs:** YouTube Data API v3 (OAuth 2.0)
- **Deployment:** Docker, Render

## Project Structure

```
youtube-comment-agent/
├── src/
│   ├── graph.py            # LangGraph StateGraph definition
│   ├── nodes.py             # fetch_comment, draft_reply, review, post_reply nodes
│   ├── state.py              # AgentState (TypedDict)
│   ├── youtube_client.py    # YouTube API: read comments, post replies, list videos
│   ├── memory.py             # Long-term memory (Postgres Store)
│   ├── checkpointer.py       # Execution persistence (Postgres Saver)
│   └── llm_utils.py          # LLM client + prompt template
├── ui/
│   └── app.py                # Streamlit approval dashboard
├── api.py                    # FastAPI entrypoint
├── client.py                 # API client helpers used by the Streamlit UI
├── requirements.txt
├── Dockerfile
└── .env                      # API keys, DB connection string (not committed)
```

## Setup

### 1. Google Cloud / YouTube API
1. Create a project at [console.cloud.google.com](https://console.cloud.google.com), enable **YouTube Data API v3**
2. Configure the OAuth consent screen (External, add yourself as a test user), scope: `youtube.force-ssl`
3. Create OAuth credentials (Desktop app), download as `credentials.json`
4. Run the token script once to authenticate and generate `token.pickle`

### 2. Supabase (Postgres)
1. Create a free project at [supabase.com](https://supabase.com)
2. Grab the connection string via the **Connect** button → Session pooler
3. Add it to `.env` as `DATABASE_URL`

### 3. Environment variables
Create a `.env` file:
```
GROQ_API_KEY=your_groq_key
DATABASE_URL=your_supabase_connection_string
```

### 4. Install & run
```bash
pip install -r requirements.txt --break-system-packages

# Terminal 1 — backend
uvicorn api:app --reload

# Terminal 2 — frontend
streamlit run ui/app.py
```

## How It Works

1. Click **"Check for new comments"** in the UI — this hits `POST /poll`
2. The agent scans your channel's videos, finds unhandled comments, and drafts a reply for each
3. Each draft appears in the dashboard with the video title and original comment
4. Click **Approve** to post the reply, or **Reject** to discard it — either way, the comment is marked as handled and won't be processed again

## Known Limitations

- `/poll` processes comments synchronously — with a high comment volume, this would need to move to an async/background-job design
- Pagination isn't yet implemented for channels with more than ~10 videos or 100+ comments per video
- No automated guardrails yet (e.g. filtering spam/vulgar comments before drafting) — currently all comments go through human review

## Roadmap

- [ ] Guardrails to auto-filter spam/inappropriate comments
- [ ] Edit-and-regenerate option instead of binary approve/reject
- [ ] Async polling + pagination for larger channels
- [ ] Optional auto-reply mode with confidence-based escalation to human review