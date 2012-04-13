from wsgifilter import Filter

from rediscounter.counter import Counter

_counter = Counter()


class CounterFilter(Filter):

    def filter(self, environ, headers, data):
        total = _counter.visit('total')
        page = _counter.visit(environ.get('PATH_INFO'))
        # Insert data at a nice place.
        text = "<p>Total: %d</p><p>This page: %d</p>" % (total, page)
        target = '<h1'
        data = data.replace(target, text + target, 1)
        return data
