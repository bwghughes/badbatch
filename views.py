from flask import Flask, render_template, make_response, request
from flask.ext.classy import FlaskView

from models import Subscriber

GOOD_SMS_RESPONSE = """<Response>
    <Sms>Thanks - you're subscribed to alerts for {}</Sms>
</Response>"""

class IndexPageView(FlaskView):
    def index(self):
        return render_template("index.html")

class RegisterView(FlaskView):
    def _create_message(self, phone_number, body):
        if phone_number and body:

            return GOOD_SMS_RESPONSE.format(body)

    def index(self):
        return "Nothing to see here. Move along."

    def post(self):
        # Add the user to the list
        phone_number = request.form.get('From')
        body = request.form.get('Body')
        sms_message = self._create_message(phone_number, body)
        response = make_response(sms_message)
        Subscriber.create(number=phone_number, location=body)
        response.headers['Content-Type'] = 'text/xml'
        return response
