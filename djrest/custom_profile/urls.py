from django.conf.urls import patterns, url

from .views import smsregister


urlpatterns = patterns('',
    url(r'^smsregister/$', smsregister, name='smsregister'),
)