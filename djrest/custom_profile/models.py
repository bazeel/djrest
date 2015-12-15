from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class UserCustomProfile(models.Model):
    user = models.OneToOneField(User, related_name='custom_profile')
    gcm_id = models.CharField(_('GCM ID'), unique=True, blank=True, max_length=255)

    class Meta:
        verbose_name = _('custom user profile')
        verbose_name_plural = _('custom user profile')
