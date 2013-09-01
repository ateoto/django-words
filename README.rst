words
============

A blog app as used by ateoto.com.

Installation
------------

To get the latest commit from GitHub

.. code-block:: bash

    $ pip install -e git+git://github.com/Ateoto/django-words.git#egg=words

TODO: Describe further installation steps (edit / remove the examples below):

Add ``words`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'words',
    )

Add the ``words`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^app-url/', include('words.urls')),
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate words


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-words
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
