#!/usr/bin/env python
import os
from random import choice

from flask.ext.script import Manager
from app import app
from main import run
from models import Subscriber, Alert, Town, Caller
from peewee import RawQuery

manager = Manager(app)

@manager.command
def createdb():
    print "Creating schema..."
    Subscriber.drop_table(fail_silently=True)
    Subscriber.create_table(fail_silently=True)
    Alert.drop_table(fail_silently=True)
    Alert.create_table(fail_silently=True)
    Caller.drop_table(fail_silently=True)
    Caller.create_table(fail_silently=True)
    seed_towns()
    print "Done."

@manager.command
def seed_towns():
    print "Seeding Towns tables..."
    towns_file = 'current/data/uk-towns-list/uk-towns.csv'
    print towns_file
    Town.drop_table(fail_silently=True)
    Town.create_table(fail_silently=True)
    rq = RawQuery(Town, "COPY uk_towns FROM '{0}' DELIMITERS ',' CSV HEADER".format(towns_file))
    try:
        rq.execute()
    except TypeError, e:
        # Wierdness here
        assert Town.select().count() == 43143


@manager.command
def create_alerts():
    drugs = ['Heroin', 'Ecstacy', 'Cocaine', 'Ketamine']
    publishers = ['Police', 'NHS', 'Shelter']
    areas = None
    alert_message = 'The {} have reported a bad batch of {} has been reported in Bolton area'


if __name__ == "__main__":
    manager.run()