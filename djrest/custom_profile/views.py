from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authtoken.models import Token


def smsregister(request):
    u = request.user
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
    # user is instance of from django.contrib.auth.models import User
    token, created = Token.objects.get_or_create(user=user)

    data = {'success': True, 'token': token.key}

    return JsonResponse(data)
