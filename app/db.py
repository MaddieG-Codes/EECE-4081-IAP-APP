import sqlite3
from pathlib import Path

from flask import current_app, g

_HERE = Path(__file__).parent


def get_db() -> sqlite3.Connection:
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(_exc=None) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db() -> None:
    """Create the schema and load seed data. Destructive: drops existing tables."""
    db = get_db()
    db.executescript((_HERE / "schema.sql").read_text())
    db.executescript((_HERE / "seed.sql").read_text())
    db.commit()
