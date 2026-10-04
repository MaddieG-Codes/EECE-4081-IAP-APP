"""End-to-end tests against a real (temporary) SQLite file. No mocks, no canned data."""

import os
import tempfile
import unittest

from app import create_app
from app.db import init_db
from app.locations import FIELDS


class WalkingSkeletonTests(unittest.TestCase):
    def setUp(self):
        fd, self.db_path = tempfile.mkstemp(suffix=".sqlite")
        os.close(fd)
        self.app = create_app({"TESTING": True, "DATABASE": self.db_path})
        with self.app.app_context():
            init_db()
        self.client = self.app.test_client()

    def tearDown(self):
        os.unlink(self.db_path)

    def test_health_touches_database(self):
        res = self.client.get("/health")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"status": "ok"})

    def test_api_returns_rows_from_sqlite(self):
        res = self.client.get("/api/locations")
        self.assertEqual(res.status_code, 200)
        locations = res.get_json()["locations"]
        self.assertGreaterEqual(len(locations), 1)
        self.assertEqual(set(locations[0]), set(FIELDS))
        self.assertEqual(locations[0]["name"], "Shelby Farms Park")

    def test_detail_page_renders_row_from_sqlite(self):
        res = self.client.get("/locations/1")
        self.assertEqual(res.status_code, 200)
        self.assertIn("Shelby Farms Park", res.get_data(as_text=True))

    def test_detail_page_404_for_unknown_id(self):
        self.assertEqual(self.client.get("/locations/9999").status_code, 404)

    def test_map_page_wires_up_the_fetch_path(self):
        res = self.client.get("/map")
        self.assertEqual(res.status_code, 200)
        html = res.get_data(as_text=True)
        self.assertIn('data-api-url="/api/locations"', html)
        with self.client.get("/static/map.js") as js:
            self.assertEqual(js.status_code, 200)

    def test_html_and_json_paths_agree(self):
        """ADR-001's named risk: two representations of one location must not drift."""
        for loc in self.client.get("/api/locations").get_json()["locations"]:
            html = self.client.get(f"/locations/{loc['id']}").get_data(as_text=True)
            for field in ("name", "city", "category", "description"):
                self.assertIn(str(loc[field]), html, f"{field} missing from detail page")


if __name__ == "__main__":
    unittest.main()
