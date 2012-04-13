import redis


def get_redis():
    # TODO: read settings from environment or similar.
    return redis.StrictRedis(host='localhost', port=6379, db=0)


class Counter(object):

    def __init__(self):
        self._db = get_redis()

    def visit(self, uid, visitor=None):
        if visitor is not None:
            self.visitor(uid, visitor)
        return self._db.incr(uid + '-visits')

    def visits(self, uid):
        return self._db.get(uid + '-visits')

    def visitor(self, uid, visitor):
        return self._db.sadd(uid + '-visitors', visitor)

    def visitors(self, uid):
        return self._db.smembers(uid + '-visitors')
