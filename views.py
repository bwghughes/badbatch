from flask import Flask, render_template
from flask.ext.classy import FlaskView


class RegisterView(FlaskView):
    def index(self):
        return render_template("index.html")
