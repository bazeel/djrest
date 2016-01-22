from django.conf.urls import url

from .views import smsregister, validatesmscode


urlpatterns = [
    url(r'^smsregister/$', smsregister, name='smsregister'),
    url(r'^validatesmscode/$', validatesmscode, name='validatesmscode'),
]
