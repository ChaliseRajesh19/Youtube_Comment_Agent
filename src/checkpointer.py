from langgraph.checkpoint.postgres import PostgresSaver
from dotenv import load_dotenv
import os

load_dotenv()

_checkpointer_cm = None
_checkpointer = None


def get_postgres_checkpointer():
    global _checkpointer_cm, _checkpointer
    if _checkpointer is not None:
        return _checkpointer
    conn_str = os.getenv("DATABASE_URL")
    _checkpointer_cm = PostgresSaver.from_conn_string(conn_str)
    _checkpointer = _checkpointer_cm.__enter__()
    _checkpointer.setup()
    return _checkpointer
