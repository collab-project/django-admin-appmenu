# Copyright Collab 2013-2016
# See LICENSE for details.

"""
URLConf for custom admin used in tests.
"""

from __future__ import unicode_literals

from .admin import admin_site

from django.conf.urls import url


urlpatterns = [
    url(r'^', admin_site.urls),
]
