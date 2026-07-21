from langgraph.store.postgres import PostgresStore
from dotenv import load_dotenv
import os

load_dotenv()

_store_cm = None
_store = None


def get_postgres_store():
    global _store_cm, _store
    if _store is not None:
        return _store
    conn_str = os.getenv("DATABASE_URL")
    _store_cm = PostgresStore.from_conn_string(conn_str)
    _store = _store_cm.__enter__()
    _store.setup()
    return _store
