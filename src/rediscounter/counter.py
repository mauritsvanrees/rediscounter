import redis


def get_redis():
    # TODO: read settings from environment or similar.
    return redis.StrictRedis(host='localhost', port=6379, db=0)


class Counter(object):

    def __init__(self):
        self._db = get_redis()

    def visit(self, key, visitor=None):
        if visitor is not None:
            self.visitor(key, visitor)
        return self._db.incr(key + '-visits')

    def visits(self, key):
        return self._db.get(key + '-visits')

    def visitor(self, key, visitor):
        return self._db.sadd(key + '-visitors', visitor)

    def visitors(self, key):
        return self._db.smembers(key + '-visitors')
