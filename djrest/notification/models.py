from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class List(models.Model):
    user = models.ManyToManyField(User, related_name='notification_lists')
    title = models.CharField(_('title'), max_length=255)
    message = models.CharField(_('message'))
    date = models.DateField(_('date'), auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _('notification list')
        verbose_name_plural = _('notification lists')


class Message(models.Model):
    date_created = models.DateField(_('date created'), auto_now_add=True)
    date_sent = models.DateField(_('date created'), null=True, blank=True)

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')
