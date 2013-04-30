#!/usr/bin/env python
from flask.ext.script import Manager
from app import app
from main import run

manager = Manager(app)

if __name__ == "__main__":
    manager.run()