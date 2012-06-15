# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

"""
Accounts application for management of the user profiles.
"""

from django.db import models
from userena.models import UserenaBaseProfile
from django.utils.translation import ugettext_lazy as _

class UserProfile(UserenaLanguageBaseProfile):

    """
    Define an extension of the user profile with fields needed in the platform.
    """
    user = models.OneToOneField(User, unique=True, verbose_name=_('User'),
                                related_name='user_profile')
    # Personal data
    name = models.CharField(_('Name'), max_length=50)
    surname = models.CharField(_('Surname'), max_length=100)
    birthdate = models.DateField(_('Birth date'))
    description = models.TextField(_('About yourself'), blank=True, null=True)

    # Other profiles
    twitter = models.URLField(_('Twitter'), max_length=255, blank=True,
                            unique=True, null=True, help_text="Insert your \
                            Twitter profile URL.")
    gplus = models.URLField(_('Google Plus'), max_length=255, blank=True,
                            unique=True, null=True, help_text="Insert your \
                            Google Plus profile URL.")
    facebook = models.URLField(_('Facebook'), max_length=255, blank=True,
                            unique=True, null=True, help_text="Insert your \
                            Facebook profile URL.")

    def get_age(self):

        """
        Calculate the user age based on the birthdate field.
        """

        if self.birthdate is not None:
            diff = datetime.date.today() - self.birthdate
            years = diff.days/365
            return years
        else:
            return '??'