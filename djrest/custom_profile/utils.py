from twilio.rest import TwilioRestClient


def sendsms(phone, message):
    # put your own credentials here
    ACCOUNT_SID = ""
    AUTH_TOKEN = ""

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_="+12018857872",
        to=phone,
        body=message,
    )
    return message

