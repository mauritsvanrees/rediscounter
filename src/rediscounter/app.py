try:
    from urlparse import parse_qs
    parse_qs  # pyflakes
except ImportError:
    # BBB Python 2.5
    from cgi import parse_qs

from rediscounter.counter import Counter

_counter = Counter()


def app(environ, start_response):
    qs = parse_qs(environ.get('QUERY_STRING', ''))
    user = qs.get('user')
    if isinstance(user, list):
        user = user[0]
    total = _counter.visit('total')
    page = _counter.visit(environ.get('PATH_INFO'), user)
    visitors = _counter.visitors(environ.get('PATH_INFO'))
    text = "<p>Total: %d</p><p>This page: %d</p><p>Visitors: %s</p>" % (
        total, page, ', '.join([v for v in visitors]))
    start_response('200 OK', [('content-type', 'text/html')])
    return [text]


def app_factory(global_config, **local_conf):
    return app
