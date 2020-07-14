# coding: utf-8

from main.database.create_database import db


def connect_to_db(config):
    db.init(
        config['DB_NAME'],
        user=config['DB_USER'],
        password=config['DB_PASS'],
        host=config['DB_HOST'],
        port=config['DB_PORT']
    )
    return db
