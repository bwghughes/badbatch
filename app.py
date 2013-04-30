import os
from flask import Flask


app = Flask(__name__)
app.config.from_object(os.environ.get('BADBATCH_SETTINGS'))
db = Database(app)


# Register views
from views import DashBoardView
RegisterView.register(app, route_base="/")





