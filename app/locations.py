"""Single source of truth for how a location is represented.

Both the Jinja2 detail page and /api/locations render from `location_to_dict`.
That keeps the two data paths from ADR-001 from drifting: add a field here and
both paths see it.
"""

from app.db import get_db

FIELDS = ("id", "name", "city", "category", "description", "latitude", "longitude")


def location_to_dict(row) -> dict:
    return {field: row[field] for field in FIELDS}


def list_locations() -> list[dict]:
    rows = get_db().execute(f"SELECT {', '.join(FIELDS)} FROM locations ORDER BY id").fetchall()
    return [location_to_dict(r) for r in rows]


def get_location(location_id: int) -> dict | None:
    row = get_db().execute(
        f"SELECT {', '.join(FIELDS)} FROM locations WHERE id = ?", (location_id,)
    ).fetchone()
    return location_to_dict(row) if row else None
