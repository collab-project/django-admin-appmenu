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

.. _pip: https://pypi.python.org/pypi/pip
.. _PyPi: https://pypi.python.org/pypi/django-admin-appmenu
.. _Github: https://github.com/collab-project/django-admin-appmenu
