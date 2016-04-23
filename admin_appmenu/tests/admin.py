# Copyright Collab 2013-2016

"""
Custom admin used for testing.
"""

from __future__ import unicode_literals

from django.conf.urls import url
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _

from django.contrib.admin import AdminSite

from .models import Location


class CustomAdminSite(AdminSite):
    site_header = 'Custom admin site'

    def custom_view(self, request):
        """
        An additional admin view.
        """
        context = dict(
           # include common variables for rendering the admin template
           self.admin_site.each_context(request),
        )
        return TemplateResponse(request, 'sometemplate.html', context)

    def get_urls(self):
        """
        Extend admin URL patterns.
        """
        urls = super(CustomAdminSite, self).get_urls()
        extra_urls = [
            url(r'^customview/$', self.custom_view, name='customview')
        ]
        return urls + extra_urls

    def get_app_list(self, request):
        app_list = super(CustomAdminSite, self).get_app_list(request)

        # categorize apps
        categorized_list = [
            {'label': _('General'), 'apps': []},
            {'label': _('Custom'), 'apps': []},
        ]

        def add_app(key, app):
            for i, dic in enumerate(categorized_list):
                if dic['label'] == key:
                    categorized_list[i]['apps'].append(app)
                    break

        for category in categorized_list:
            for app in app_list:
                name = app['name']
                label = category['label']
                if label == _('General'):
                    if name in ['Admin_Appmenu']:
                        add_app(label, app)

        # add custom links for superusers
        if request.user.is_superuser:
            categorized_list[1]['apps'].append(
                {
                    'name': _('Custom views'),
                    'models': [
                    {
                        'name': _('My custom view'),
                        'admin_url': reverse('admin:customview')
                    }
                ]}
            )
        else:
            categorized_list = []

        return categorized_list


admin_site = CustomAdminSite(name='customadmin')
admin_site.register(Location)
