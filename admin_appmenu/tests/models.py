# Copyright Collab 2016

"""
Models used for testing.
"""

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Location(models.Model):
    """
    Location.
    """
    name = models.CharField(
        _('name'),
        help_text=_('Name of the location.'),
        max_length=255,
        blank=False,
        null=False
    )
    slug = models.SlugField(
        _('slug'),
        help_text=_('Location name as used in links.'),
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )
    address = models.CharField(
        _('address'),
        help_text=_('Location address.'),
        max_length=255,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')

    def __str__(self):
        return self.name
