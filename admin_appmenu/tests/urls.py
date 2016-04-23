# Copyright Collab 2015-2016
# See LICENSE for details.

"""
URLConf for :py:mod:`admin_footer` tests.
"""

from __future__ import unicode_literals

from django.contrib import admin
from django.conf.urls import url


admin.autodiscover()

urlpatterns = [
    url(r'^', admin.site.urls),
]
