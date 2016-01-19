from django.conf.urls import url

from .views import smsregister


urlpatterns = [
    url(r'^smsregister/$', smsregister, name='smsregister'),
]
