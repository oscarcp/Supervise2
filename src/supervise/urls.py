# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.utils.translation import ugettext_lazy as _

admin.autodiscover()

urlpatterns = patterns('',

    # url(r'^$', 'supervise.views.home', name='home'),

    # url(r'^supervise/', include('supervise.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # User accounts URLs
    url(r'^u/', include('apps.thirdparty.userena.urls')),

)

if settings.DEBUG:
    # Serve static files
    urlpatterns += staticfiles_urlpatterns()
    # Serve uploaded files
    urlpatterns += patterns('',
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    )
