from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class UserCustomProfile(models.Model):
    user = models.OneToOneField(User, related_name='custom_profile')
    gcm_id = models.CharField(_('GCM ID'), unique=True, null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = _('custom user profile')
        verbose_name_plural = _('custom user profile')


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
