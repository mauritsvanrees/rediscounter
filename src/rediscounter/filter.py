from wsgifilter import Filter

from rediscounter.counter import Counter

_counter = Counter()


class CounterFilter(Filter):
    def filter(self, environ, headers, data):
        print _counter.visit('total')
        return data
