class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.cache = dict()
        self.capacity = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    @staticmethod
    def _remove_node(node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _remove_oldest(self):
        if len(self.cache) > 0:
            oldest_node = self.tail.prev
            self._remove_node(oldest_node)
            del self.cache[oldest_node.key]

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        return

    @property
    def cache1(self):
        node = self.tail.prev
        self._move_to_front(node)
        return node.value

    @cache1.setter
    def cache1(self, val):
        key, value = val
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
            return
        if len(self.cache) >= self.capacity:
            self._remove_oldest()
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)

    @property
    def size(self):
        return len(self.cache)

    @property
    def keys(self):
        return list(self.cache.keys())

    def __str__(self):
        res = "{"
        cur = self.head.next
        for v in range(self.size):
            res += str(cur.key) + ": " + str(cur.value)
            cur = cur.next
            if v != self.size - 1:
                res += ", "
                continue
            res += "}"
        return res


if __name__ == "__main__":
    cache = LRUCache(5)

    cache.cache1 = (1, 1)
    cache.cache1 = (2, 2)
    cache.cache1 = (3, 3)
    cache.cache1 = (4, 4)
    cache.cache1 = (5, 5)
    print(cache)

    print(cache.cache1)
    print(cache.cache1)
    print(cache.cache1)
    print(cache.get(5))

    cache.cache1 = (6, 6)

    print(cache)
