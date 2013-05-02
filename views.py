from flask import Flask, render_template, make_response, request
from flask.ext.classy import FlaskView

from models import Subscriber, Caller, Alert

GOOD_SMS_RESPONSE = """
<Response>
    <Sms>Thanks - you're subscribed to alerts for {}</Sms>
</Response>
"""

WELCOME_MESSAGE = """
<Response>
    <Play>https://dl.dropboxusercontent.com/u/246389/badbatch/welcome_message.mp3</Play>
    <Dial>+447427600266</Dial>
</Response>
"""

BAD_BATCH_NUMBER = "+44 20 0333 1508"


class IndexPageView(FlaskView):
    def index(self):
        return render_template("index.html", number=BAD_BATCH_NUMBER)


class AlertsView(FlaskView):
    def index(self):
        return render_template("alerts.html")


class ContactView(FlaskView):
    def index(self):
        return render_template("contacts.html",
                               number=BAD_BATCH_NUMBER)


class CallView(FlaskView):
    def post(self):
        phone_number = request.form.get('From')
        response = make_response(WELCOME_MESSAGE)
        Caller.create(number=phone_number)
        response.headers['Content-Type'] = 'text/xml'
        return response


class RegisterView(FlaskView):
    def _create_message(self, phone_number, body):
        if phone_number and body:
            return GOOD_SMS_RESPONSE.format(body)

    def post(self):
        # Add the user to the list
        phone_number = request.form.get('From')
        body = request.form.get('Body')
        sms_message = self._create_message(phone_number, body)
        response = make_response(sms_message)
        Subscriber.create(number=phone_number, location=body)
        response.headers['Content-Type'] = 'text/xml'
        return response
