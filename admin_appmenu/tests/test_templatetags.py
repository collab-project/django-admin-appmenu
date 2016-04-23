# Copyright Collab 2013-2016

"""
Tests for the :py:mod:`admin_appmenu.templatetags`.
"""

from __future__ import unicode_literals

import os

from django.template import base, loader
from django.template.context import Context
from django.test.utils import override_settings
from django.test import TestCase, RequestFactory

from django.contrib.auth.models import User

from ..util import get_admin_site


custom_template_dir = os.path.join(os.path.dirname(__file__), 'templates')


class DefaultNavigationTagTestCase(TestCase):
    """
    Tests for the :py:mod:`admin_appmenu.templatetags.navigation` template tag.

    By default it uses the built-in Django admin site.
    """
    template = 'admin_appmenu/navigation.html'
    empty_result = '<ul>\n\n</ul>'

    def setUp(self):
        self.username = 'notstaff'
        self.password = 'top_secret'
        self.email = 'foo@bar'

    def get_context(self, user):
        request = RequestFactory().post('/', user=user)
        request.user = user
        context = {'request': request}
        return context

    def _renderTemplate(self, request={}):
        data = {}
        admin = get_admin_site()
        data = {'nav_list': admin.get_app_list(request)}

        tpl = loader.get_template(self.template)
        return tpl.render(data)

    def assertNavigation(self, context, output,
                         template='{% admin_navigation %}'):
        """
        Ensure rendered template is correct.

        :param template:
        :param context:
        :param output:
        """
        template = base.Template('{% load navigation %}' + template)
        ctx = Context(context)
        self.assertEqual(template.render(ctx), output)

    def test_navigationStaff(self):
        """
        Using the tag with admin rights returns a list.
        """
        user = User.objects.create_superuser(self.username, self.email,
            self.password)
        context = self.get_context(user)
        output = self._renderTemplate(context['request'])

        self.assertNavigation(context, output)

    def test_navigationNotStaff(self):
        """
        Using the tag without (admin) rights returns an empty list.
        """
        user = User.objects.create_user(self.username, self.email,
            self.password)
        context = self.get_context(user)
        output = self.empty_result

        self.assertNavigation(context, output)

    def test_missingRequestInContext(self):
        """
        Using the tag without passing a 'request' to the context returns
        an empty list.
        """
        context = {}
        output = self.empty_result

        self.assertNavigation(context, output)

    def test_rejectArguments(self):
        """
        Passing arguments to the tag raises a ``TemplateSyntaxError``.
        """
        try:
            base.Template('{% load navigation %}{% admin_navigation foo %}')
        except base.TemplateSyntaxError as e:
            self.assertEqual(str(e),
                'admin_navigation tag does not accept any argument(s): foo')



class CustomAdminNavigationTagTestCase(DefaultNavigationTagTestCase):
    """
    The tag also works with a custom admin and template.
    """
    empty_result = ''

    def run(self, *args, **kwargs):
        with override_settings(
            # use custom admin site
            ADMIN_APPMENU_CLASS='admin_appmenu.tests.admin.admin_site',
            ROOT_URLCONF='admin_appmenu.tests.custom_admin_urls',
            # add custom templates directory for this test
            TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [custom_template_dir]
            }]
        ):
            return super(CustomAdminNavigationTagTestCase, self).run(*args, **kwargs)
