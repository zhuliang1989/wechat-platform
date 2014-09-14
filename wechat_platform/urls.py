# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^admin/', include('admin.urls', namespace='admin')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)