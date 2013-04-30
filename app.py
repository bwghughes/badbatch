import os
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_object(os.environ.get('BADBATCH_SETTINGS'))
Bootstrap(app)
db = Database(app)

# Register views
from views import RegisterView, IndexPageView
IndexPageView.register(app, route_base="/")
RegisterView.register(app, route_base="/register")





