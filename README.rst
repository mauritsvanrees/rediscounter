Redis Counter
=============

At the moment this is a toy project, a proof of concept.

The main idea is that we use Redis_ to keep a few counters of
visits to web pages.

There are a few elements in this code:

- A ``bootstrap.py`` and ``buildout.cfg`` so you can use buildout_ to
  set everything up for testing.

- A Redis_ server, setup by buildout.

- A ``rediscounter`` Python package, with some code for increasing a
  counter in Redis and getting its value (hardly rocket science) using
  the redis_ Python package, and some WSGI code.

- A Paste server that uses the filter from this ``rediscounter``
  package.  Start it with ``bin/paster serve --reload devel.ini``.  It
  is currently setup to serve on http://127.0.0.1:4000/.  It gets html
  from http://zestsoftware.nl/ as an example.  While doing this, it
  updates a total counter and a count of visits to the current page.
  It inserts those statistics into the html, to show that it is active
  and working.

.. _Redis: http://redis.io/
.. _buildout: http://www.buildout.org/
.. _redis: http://pypi.python.org/pypi/redis
