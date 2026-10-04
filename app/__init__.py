from pathlib import Path

import click
from flask import Flask

from app import db, routes


def create_app(config: dict | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config["DATABASE"] = str(Path(app.instance_path) / "explorer.sqlite")
    if config:
        app.config.update(config)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    app.teardown_appcontext(db.close_db)
    app.register_blueprint(routes.bp)

    @app.cli.command("init-db")
    def init_db_command():
        """Create tables and load seed data (destructive)."""
        db.init_db()
        click.echo("Initialized the database.")

    return app
