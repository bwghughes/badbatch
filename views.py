from flask import Flask, render_template, make_response, request
from flask.ext.classy import FlaskView

SMS_RESPONSE = """<Response>
    <Sms>Cheers duck</Sms>
</Response>"""

class IndexPageView(FlaskView):
    def index(self):
        return render_template("index.html")

class RegisterView(FlaskView):
    def index(self):
        return "Nothing to see here. Move along."

    def post(self):
        # Add the user to the list
        print request.form
        response = make_response(SMS_RESPONSE)
        response.headers['Content-Type'] = 'text/xml'
        return response