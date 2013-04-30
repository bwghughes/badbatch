from app import db
import datetime
from peewee import CharField, DateTimeField


class Subscriber(db.Model):
    number = CharField()
    location = CharField()
    created_at = DateTimeField(default=datetime.datetime.now())
