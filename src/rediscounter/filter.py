from wsgifilter import Filter

from rediscounter.counter import Counter

_counter = Counter()


class CounterFilter(Filter):

    def filter(self, environ, headers, data):
        _counter.visit('total')
        _counter.visit(environ.get('PATH_INFO'))
        return data
