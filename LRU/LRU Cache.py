class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.times = 0
        self.num = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.cache[key][1] = self.times
            self.times += 1
            return self.cache[key][0]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache:
            self.num += 1
        self.cache[key] = [value, self.times]
        self.times += 1

        if self.num > self.capacity:
            minTimeKey = None
            minTime = 1<<32
            for key in self.cache:
                if self.cache[key][1] < minTime:
                    minTime = self.cache[key][1]
                    minTimeKey = key
            self.cache.pop(minTimeKey)
            self.num -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node(object):
    def __init__(self, key, value):
        """
        :type key: int, value: int
        """
        self.key = key
        self.value = value
        self.prev = self
        self.next = self

class LRUCacheV1(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        :note: linkedList version
        """
        self.cap = capacity
        self.cache = Node(None, None)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        n = self.cache
        while n.next != self.cache:
            n = n.next
            if n.key == key:
                # move n after self.cache
                n.prev.next, n.next.prev = n.next, n.prev
                n.next, n.prev = self.cache.next, self.cache
                self.cache.next, n.next.prev = n, n
                return n.value
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        n = self.cache
        count = 0
        while n.next != self.cache:
            n = n.next
            count += 1
            if n.key == key:
                n.value = value
                # move n after self.cache
                n.prev.next, n.next.prev = n.next, n.prev
                n.next, n.prev = self.cache.next, self.cache
                self.cache.next, n.next.prev = n, n
                return

        if count == self.cap:
            # delete n
            n.prev.next = n.next
            n.next.prev = n.prev
            del n

        # insert new Node after self.cache
        newNode = Node(key, value)
        newNode.next = self.cache.next
        newNode.next.prev = newNode
        self.cache.next = newNode
        newNode.prev = self.cache


class LRUCacheV2(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = Node(None, None)
        self.map = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            n = self.map[key]
            # move n after self.cache
            n.prev.next, n.next.prev = n.next, n.prev
            n.next, n.prev = self.cache.next, self.cache
            self.cache.next, n.next.prev = n, n
            return n.value
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            n = self.map[key]
            n.value = value
            # move n after self.cache
            n.prev.next, n.next.prev = n.next, n.prev
            n.next, n.prev = self.cache.next, self.cache
            self.cache.next, n.next.prev = n, n
            return
        else:
            if len(self.map) == self.cap:
                n = self.cache.prev
                # delete n
                n.prev.next = n.next
                n.next.prev = n.prev
                # delete in map
                self.map.pop(n.key)
                del n
            # insert new Node after self.cache
            newNode = Node(key, value)
            self.map[key] = newNode
            newNode.next = self.cache.next
            newNode.next.prev = newNode
            self.cache.next = newNode
            newNode.prev = self.cache





