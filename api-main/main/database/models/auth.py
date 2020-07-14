# coding: utf-8

import hashlib
from flask import current_app
from peewee import (BooleanField, DateTimeField, Model, PrimaryKeyField,
                    TextField)
from datetime import datetime
from main.database.create_database import db


class Users(Model):
    class Meta:
        database = db

    id = PrimaryKeyField()
    user = TextField()
    password = TextField()
    active = BooleanField(default=True)
    created = DateTimeField(default=datetime.now())

    def _create_user(self, user, password):
        salt = current_app.config['SECRET_KEY']
        hashed_pass = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), salt, 100000)
        self.create(user=user, password=hashed_pass)
