from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class List(models.Model):
    users = models.ManyToManyField(User, blank=True, related_name='notification_lists')
    title = models.CharField(_('title'), max_length=255)
    text = models.TextField(_('message text'))
    date = models.DateTimeField(_('date'), auto_now_add=True)
    processed = models.BooleanField(_('processed'), default=False)

    def __unicode__(self):
            return self.title + ' ' + self.date.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        ordering = ['-date']
        verbose_name = _('notification list')
        verbose_name_plural = _('notification lists')


class Message(models.Model):
    list = models.ForeignKey(List, related_name='messages')
    user = models.ForeignKey(User, related_name='messages')
    title = models.CharField(_('title'), max_length=255)
    text = models.TextField(_('message text'))
    success = models.BooleanField(_('success'), default=False)
    response = models.TextField(_('response from GCM'), blank=True, null=True)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_sent = models.DateTimeField(_('date sent'), null=True, blank=True)
    attempt = models.PositiveSmallIntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')
