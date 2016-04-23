# Copyright Collab 2013-2016
# See LICENSE for details.

"""
Tests for the :py:mod:`admin_appmenu` versioning.
"""

from __future__ import unicode_literals

from django.test import TestCase

from admin_appmenu import get_version


class VersionTestCase(TestCase):
    """
    Tests for :py:mod:`~admin_appmenu` versioning information.
    """
    def test_regularVersion(self):
        """
        :py:func:`~admin_appmenu.get_version` returns a string version without
        any beta tags, eg. ``1.0.1``.
        """
        version = (1, 0, 1)
        self.assertEqual(get_version(version), '1.0.1')

    def test_betaVersion(self):
        """
        :py:func:`~admin_appmenu.get_version` returns a string version with
        beta tags, eg. ``1.2.3b1``.
        """
        version = (1, 2, 3, 'b1')
        self.assertEqual(get_version(version), '1.2.3b1')
