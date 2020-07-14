# coding: utf-8

from flask import Flask
from flask_cors import CORS
from main.config import config_meta
from main.database.connect_to_database import connect_to_db
from main.database.models.auth import Users


def create_app(cfg='dev'):
    app = Flask(__name__)
    CORS(app)
    config = config_meta.get(cfg)
    app.config.from_object(config)
    app.database = connect_to_db(app.config)
    create_tables(app.database)
    return app


def create_tables(db):
    models = [Users]
    to_create = [model for model in models if not db.table_exists(
        model._meta.table_name)]
    db.create_tables(to_create)
