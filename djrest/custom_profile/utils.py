from twilio.rest import TwilioRestClient
from django.conf import settings


def sendsms(phone_to, message):
    # put your own credentials here
    account_sid = settings.TWILIO.ACCOUNT_SID
    auth_token = settings.TWILIO.AUTH_TOKEN
    phone_from = settings.TWILIO.FROM

    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(
        from_=phone_from,
        to=phone_to,
        body=message,
    )
    return message

