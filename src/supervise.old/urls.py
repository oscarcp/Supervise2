#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    supervise.urls
    ~~~~~~~~~~~~~~

    This file distributes all the URLs around Supervise apps.

    :copyright: (c) 2011 by Oscar Carballal Prego <oscarcp@clionesoftware.com>
    :license: Simplified BSD License, see LICENSE for more details.
"""

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

admin.autodiscover()

urlpatterns = patterns('',

    # Django administration interface
    url(r'^admin/', include(admin.site.urls)),

    # Uploads content #### FOR DEVELOPMENT!! ####
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_URL}),

    # User accounts
    url(r'^user/', include('supervise.apps.userprofile.urls'), name='user'),
    
    # Supervise index
    #url(r'^$', 'supervise.views.home'),
    
    # i18n language switcher
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # Project index    
    #url(r'^(?P<project_name>[\w\-]+)/', include('supervise.apps.projects.urls'),
    #    name='projects'),
)

urlpatterns += staticfiles_urlpatterns()