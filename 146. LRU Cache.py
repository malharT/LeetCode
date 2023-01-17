class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.cap = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.store:
            cur_tup = self.store[key]
            val, f, b = cur_tup[0], cur_tup[1], cur_tup[2]
            if f is None:
                return val
            self.store[f][2] = b
            if b is not None:
                self.store[b][1] = f
            else:
                self.tail = f
            self.store[self.head][1] = key
            self.store[key][2] = self.head
            self.store[key][1] = None
            self.head = key
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.store:
            if len(self.store) == self.cap:
                cur_tail = self.store[self.tail]
                del self.store[self.tail]
                if self.tail != self.head:
                    f = cur_tail[1]
                    self.store[f][2] = None
                    self.tail = f
                else:
                    self.tail = None
                    self.head = None
            if self.head is not None:
                self.store[self.head][1] = key
            self.store[key] = [value, None, self.head]
            self.head = key
            if self.tail is None:
                self.tail = key
        else:
            self.get(key)
            self.store[key][0] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)