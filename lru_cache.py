import collections
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self._d = collections.OrderedDict()

    def get(self, key):
        if key in self._d.keys():
            self._d.move_to_end(key)
            return self._d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self._d) >= self.capacity:
            self._d.popitem(0)
            self._d[key] = value
        else:
            self._d[key] = value


lru = LRUCache(2)
lru.put(2, 1)
lru.put(1, 5)
lru.put(1, 2)
lru.get(1)
lru.get(2)
print(lru.get(2))
ls = set()
