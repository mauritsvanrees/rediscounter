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
  the `redis Python package`, and some WSGI code.

- A Paste server with two pipelines.  Start it with ``bin/paster serve
  --reload devel.ini``.  It is currently setup to serve on
  http://127.0.0.1:4000/.

- One Paste pipelins is the filter from this ``rediscounter`` package.
  It gets html from http://zestsoftware.nl/ as an example.  While
  doing this, it updates a total counter and a count of visits to the
  current page.  It inserts those statistics into the html, to show
  that it is active and working.

- A second Paste pipeline is a simple app that only updates counters,
  without giving back upstream html.  You could target this with some
  javascript that does a POST to
  http://127.0.0.1:4000/count?user=maurits&uid=abcde.  This counts as
  one visit by user maurits to an object with unique id abcde.
  http://127.0.0.1:4000/count/my/path?user=maurits will be counted as
  a visit by maurits to unique id /my/path.  Note that when a uid
  query string is set, the path is ignored.  When no user is given, it
  is counted anonymously.

.. _Redis: http://redis.io/
.. _buildout: http://www.buildout.org/
.. _`redis Python package`: http://pypi.python.org/pypi/redis
