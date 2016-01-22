import re
from twilio.rest import TwilioRestClient
from django.conf import settings


def sendsms(phone_to, message):
    # put your own credentials here
    account_sid = settings.TWILIO.get('ACCOUNT_SID')
    auth_token = settings.TWILIO.get('AUTH_TOKEN')
    phone_from = settings.TWILIO.get('FROM')

    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(
        from_=phone_from,
        to=phone_to,
        body=message,
    )
    return message


def validatephone(phone):
    prog = re.compile('^\d{10}$')
    result = prog.match(phone)
    if not result:
        raise Exception('Phone number is not valid')
