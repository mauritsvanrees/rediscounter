try:
    from urlparse import parse_qs
    parse_qs  # pyflakes
except ImportError:
    # BBB Python 2.5
    from cgi import parse_qs

from rediscounter.counter import Counter

_counter = Counter()

TEXT = """
<p>User %(user)s visits page %(uid)r</p>
<p>Total: %(total)d</p>
<p>This page: %(page_total)d</p>
<p>Visitors: %(visitors)s</p>"""


def app(environ, start_response):
    qs = parse_qs(environ.get('QUERY_STRING', ''))
    # Get a user from the query parameters.
    user = qs.get('user')
    if isinstance(user, list):
        user = user[0]
    # Get a unique id for which we should update the counter.
    uid = qs.get('uid')
    if isinstance(uid, list):
        uid = uid[0]
    if not uid:
        # Fall back to the path info for the unique id.
        uid = environ.get('PATH_INFO')
    total = _counter.visit('total')
    page_total = _counter.visit(uid, user)
    visitors = _counter.visitors(uid)
    text = TEXT % dict(
        user=user is None and 'Anonymous' or user,
        uid=uid,
        total=total,
        page_total=page_total,
        visitors=', '.join([v for v in visitors]),
        )
    start_response('200 OK', [('content-type', 'text/html')])
    return [text]


def app_factory(global_config, **local_conf):
    return app
