from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class UserList(models.Model):
    users = models.ManyToManyField(User, blank=True, related_name='notification_lists')
    title = title = models.CharField(_('title'), max_length=255)
    date_created = models.DateTimeField(_('date'), auto_now_add=True)

    def __unicode__(self):
            return self.title

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('notification users list')
        verbose_name_plural = _('notification users lists')


class Message(models.Model):
    user_list = models.ForeignKey(UserList, related_name='messages')
    title = models.CharField(_('title'), max_length=255)
    text = models.TextField(_('message text'))
    processed = models.BooleanField(_('processed'), default=False)
    date_created = models.DateTimeField(_('date'), auto_now_add=True)

    def __unicode__(self):
            return str(self.id) + ' ' + self.title

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('message')
        verbose_name_plural = _('messages')


class MessageLog(models.Model):
    message = models.ForeignKey(Message, related_name='log')
    user = models.ForeignKey(User, related_name='log')
    title = models.CharField(_('title'), max_length=255)
    text = models.TextField(_('message text'))
    success = models.BooleanField(_('success'), default=False)
    response = models.TextField(_('response from GCM'), blank=True, null=True)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_sent = models.DateTimeField(_('date sent'), null=True, blank=True)
    attempt = models.PositiveSmallIntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('logged message')
        verbose_name_plural = _('logged messages')
