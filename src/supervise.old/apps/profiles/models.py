#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    supervise.apps.profiles.models
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This file defines all the data models for extending the default django user
    profile.

    :copyright: (c) 2011 by Oscar Carballal Prego <oscarcp@clionesoftware.com>
    :license: Simplified BSD License, see LICENSE for more details.
"""
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from supervise.apps.userprofile.models import BaseProfile

GENDER = (
    
    ('M', _('Male')),
    ('F', _('Female')),
    ('U', _('Unknown')),

)

class UserProfile(BaseProfile):
    firstname = models.CharField(_('Name'), max_length=50, blank=True)
    lastname = models.CharField(_('Last name'), max_length=200, blank=True)
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER,
                              blank=True)
    birthdate = models.DateField(_('Birth date'), blank=True, null=True)
    email = models.EmailField(_('Email'), unique=True)
    website = models.URLField(_('Website'), verify_exists=True, max_length=100,
                              null=True, blank=True,
                              help_text=_('The URL will be veryfied.'))
    
    def get_age(self):
        
        """
        Get current user age.
        """
        if self.birthdate is not None:
            diff = datetime.date.today() - self.birthdate
            years = diff.days/365
            return years
        else:
            return _('Unknown')
            
    def __unicode__(self):
        return self.firstname + self.lastname