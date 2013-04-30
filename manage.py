#!/usr/bin/env python
from flask.ext.script import Manager
from app import app
from main import run
from models import Subscriber

manager = Manager(app)

@manager.command
def createdb():
    print "Creating schema..."
    Subscriber.drop_table(fail_silently=True)
    Subscriber.create_table(fail_silently=True)
    print "Done."


if __name__ == "__main__":
    manager.run()