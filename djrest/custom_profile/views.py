import json
from random import randint
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import UserCustomProfile
from .utils import sendsms


# post json {'phone': 1234567}
@csrf_exempt
def smsregister(request):
    '''
    if u.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    user_form = UserForm()
    success = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_data = user_form.cleaned_data
            try:
                user = User.objects.create_user(
                    user_data['username'],
                    user_data['email'],
                    user_data['password'])
            except Exception:
                pass
            else:
                code = InvitationCode.objects.get(code=user_data['invitation_code'])
                profile = UserProfile(user=user, invitation_code=code)
                profile.save()
                user.first_name = user_data['first_name']
                user.last_name = user_data['last_name']
                user.save()
                success = True
                user_form = UserForm()
    '''

    try:
        if request.method == 'POST':
            received_json_data = json.loads(request.body)
            phone = received_json_data.get('phone')
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

            #TODO validate number
            message = sendsms(phone, smscode)

            data = {'success': True}

        else:
            data = {'success': False}

    except Exception as e:
        msg = '%s (%s)' % (e.message, type(e))
        data = {'success': False, 'message': msg}

    return JsonResponse(data)


@csrf_exempt
def validatesmscode(request):

    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        username = received_json_data.get('phone')
        smscode = received_json_data.get('smscode')
        user = User.objects.get(username=username)
        # TODO reset sms code after checking
        # TODO if code is valid
        #if :
        #    token, token_created = Token.objects.get_or_create(user=user)
        #    data = {'success': True, 'authtoken': token.key}

    data = {'success': False}

    return JsonResponse(data)
