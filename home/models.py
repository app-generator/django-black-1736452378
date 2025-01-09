# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Game(models.Model):

    #__Game_FIELDS__
    appid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    playtime_2weeks = models.IntegerField(null=True, blank=True)
    playtime_forever = models.IntegerField(null=True, blank=True)
    playtime_windows_forever = models.IntegerField(null=True, blank=True)
    playtime_mac_forever = models.IntegerField(null=True, blank=True)
    playtime_linux_forever = models.IntegerField(null=True, blank=True)
    playtime_deck_forever = models.IntegerField(null=True, blank=True)
    rtime_last_played = models.IntegerField(null=True, blank=True)
    playtime_disconnected = models.IntegerField(null=True, blank=True)
    img_icon_url = models.TextField(max_length=255, null=True, blank=True)
    acquired_date = models.TextField(max_length=255, null=True, blank=True)

    #__Game_FIELDS__END

    class Meta:
        verbose_name        = _("Game")
        verbose_name_plural = _("Game")



#__MODELS__END
