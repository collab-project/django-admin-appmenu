# Copyright Collab 2013-2016

"""
Navigation template tags for the :py:mod:`admin_appmenu` application.
"""

from __future__ import unicode_literals

import logging

from django import template
from django.template import base, loader

from ..util import get_admin_site


register = template.Library()
logger = logging.getLogger(__name__)


class AdminUserNavigationNode(template.Node):
    """
    Build navigation tree with the admin's :py:func:`get_app_list` and render
    the resulting context into the navigation template.
    """
    def render(self, context):
        data = None
        try:
            admin = get_admin_site()
            data = admin.get_app_list(context['request'])
        except (ValueError, KeyError):
            pass
        except Exception as e:  # pragma: no cover
            logger.exception(e)

        tpl = loader.get_template('admin_appmenu/navigation.html')
        return tpl.render({'nav_list': data})


@register.tag
def admin_navigation(parser, token):
    """
    Template tag that renders the main admin navigation tree based on the
    authenticated user's permissions.
    """
    # split_contents() knows not to split quoted strings.
    tag_name = token.split_contents()

    if len(tag_name) > 1:
        raise base.TemplateSyntaxError(
            '{} tag does not accept any argument(s): {}'.format(
            token.contents.split()[0],
            ', '.join(token.contents.split()[1:])
    ))

    return AdminUserNavigationNode()
