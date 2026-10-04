from flask import Blueprint, abort, jsonify, render_template

from app.db import get_db
from app.locations import get_location, list_locations

bp = Blueprint("main", __name__)
@bp.get("/")
def home():
    return "Southern City Explorer is running!"


@bp.get("/health")
def health():
    get_db().execute("SELECT 1").fetchone()  # proves the DB connection, not just Flask
    return jsonify(status="ok")


# --- Server-rendered path (Jinja2) ---------------------------------------------
@bp.get("/locations/<int:location_id>")
def location_detail(location_id: int):
    location = get_location(location_id)
    if location is None:
        abort(404)
    return render_template("location_detail.html", location=location)


@bp.get("/map")
def map_view():
    # Shell only: the locations arrive via fetch() from /api/locations.
    return render_template("map.html")


# --- JSON path (map + search/filter only, per ADR-001) -------------------------
@bp.get("/api/locations")
def api_locations():
    return jsonify(locations=list_locations())
