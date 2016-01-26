import json
from random import randint
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import UserCustomProfile
from .utils import sendsms, validatephone


# post json 10 digits number {"phone": "0123456789"}
@csrf_exempt
def smsregister(request):
    try:
        if request.method == 'POST':
            received_json_data = json.loads(request.body)
            phone = received_json_data.get('phone')
            validatephone(phone)
            username = phone
            password = User.objects.make_random_password()
            user, user_created = User.objects.get_or_create(
                username=username,
                email=settings.DEFAULT_USER_EMAIL,
            )
            user.set_password(password)
            profile, profile_created = UserCustomProfile.objects.get_or_create(user=user)
            smscode = randint(1000, 9999)
            profile.sms_code = smscode
            profile.save()
            user.save()

            phone = '+7' + phone
            msg = 'CODE: %s' % smscode
            message = sendsms(phone, msg)

            data = {'success': True}

        else:
            data = {'success': False}

    except Exception as e:
        msg = '%s (%s)' % (e.message, type(e))
        data = {'success': False, 'message': msg}

    return JsonResponse(data)


# post json {"phone":"0123456789", "smscode": "1234"}
@csrf_exempt
def validatesmscode(request):
    data = {}
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        username = received_json_data.get('phone')
        smscode = received_json_data.get('smscode')
        user = User.objects.get(username=username)

        if user.custom_profile.sms_code and user.custom_profile.sms_code == smscode:
            token, token_created = Token.objects.get_or_create(user=user)
            data = {'success': True, 'authtoken': token.key}
        else:
            data = {'success': False, 'message': 'Invalid sms code'}

        #reset sms code
        profile = UserCustomProfile.objects.get(user=user)
        profile.sms_code = None
        profile.save()

    return JsonResponse(data)
