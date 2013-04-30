from flask import Flask, render_template
from flask.ext.classy import FlaskView
from flask.ext.security import login_required
from models import Site


class RegisterView(FlaskView):
    @login_required
    def index(self):
        return render_template("index.html")
