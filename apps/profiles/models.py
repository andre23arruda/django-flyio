from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    '''User Profile model'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    phone = models.CharField(max_length=19, blank=True, verbose_name=_('Phone'))
    birth_date = models.DateField(blank=True, null=True, verbose_name=_('Birth date'))
    avatar = models.URLField(max_length=200, blank=True, help_text='Avatar URL', verbose_name=_('Avatar'))

    class Meta:
        app_label = 'auth'
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return f'{ self.user }'
