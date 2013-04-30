import os
from flask import Flask
from flask.ext.security import Security, SqlAlchemyUserDatastore
from flask_mail import Mail
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(os.environ.get('ROOMYUI_SETTINGS'))
db = Database(app)
mail = Mail(app)

# Show Toolbar in Dev Mode
if app.debug:
    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension(app)

# Register Security
from models import User, Role, UserRoles
user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)

# Register views
from views import DashBoardView
DashBoardView.register(app, route_base="/")





