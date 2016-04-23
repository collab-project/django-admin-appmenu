django-admin-appmenu
====================

``django-admin-appmenu`` provides a templatetag that renders an application
menu in the `Django <https://www.djangoproject.com>`_  admin.

.. image:: https://img.shields.io/pypi/v/django-admin-appmenu.svg
    :target: https://pypi.python.org/pypi/django-admin-appmenu
.. image:: https://img.shields.io/pypi/pyversions/django-admin-appmenu.svg
    :target: https://pypi.python.org/pypi/django-admin-appmenu
.. image:: https://travis-ci.org/collab-project/django-admin-appmenu.svg?branch=master
    :target: https://travis-ci.org/collab-project/django-admin-appmenu
.. image:: https://coveralls.io/repos/collab-project/django-admin-appmenu/badge.svg
    :target: https://coveralls.io/r/collab-project/django-admin-appmenu
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/collab-project/django-admin-appmenu/master/LICENSE

Installation
------------

Use pip_ to install the download and install the package from PyPi_::

  pip install django-admin-appmenu

Or checkout the source code from Github_::

  git clone https://github.com/collab-project/django-admin-appmenu.git
  cd django-admin-appmenu
  pip install -e .

Add ``admin_appmenu`` to ``INSTALLED_APPS`` in your Django project settings:

.. code-block:: python

  INSTALLED_APPS = (
      ...

      'admin_appmenu',
  )

Usage
-----

Override_ the ``admin/base.html`` template and make the tag available in the
template:

.. code-block:: python

  {% load navigation %}


Now add the ``admin_navigation`` tag to the template:

.. code-block:: python

  {% admin_navigation %}

After reloading the admin you will see the new menu.

To customize the output of the tag create and customize a copy of the
``admin_appmenu/navigation.html`` template.

Custom admin site
-----------------

By default the standard Django admin site (``django.contrib.admin.site``)
is used to build the menu tree. If your project uses a `customized admin site`_
set the ``ADMIN_APPMENU_CLASS`` setting to the path of the custom admin site
instance.

For example in ``settings.py``:

.. code-block:: python

  ADMIN_APPMENU_CLASS = 'myapp.admin.admin_site'

This also allows you to `sort and format`_ the applications list used to render
the menu.

.. _pip: https://pypi.python.org/pypi/pip
.. _PyPi: https://pypi.python.org/pypi/django-admin-appmenu
.. _Github: https://github.com/collab-project/django-admin-appmenu
.. _override: https://docs.djangoproject.com/en/1.9/ref/contrib/admin/#overriding-admin-templates
.. _customized admin site: https://docs.djangoproject.com/en/1.9/ref/contrib/admin/#customizing-the-adminsite-class
.. _sort and format: https://github.com/collab-project/django-admin-appmenu/blob/master/admin_appmenu/tests/admin.py#L42