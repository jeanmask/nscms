#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('nscms.contrib.newsletter.views',
    url(r'^optin/$', 'optin', name="optin"),
)
