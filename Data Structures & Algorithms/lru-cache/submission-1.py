class LRUCache:

    def __init__(self, capacity: int):
        self.lookup = {}
        self.capacity = capacity
        self.q = []

    def get(self, key: int) -> int:
        if key in self.lookup: 
            self.q.append(key)
            return self.lookup[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        self.q.append(key)
        if key in self.lookup:
            self.lookup[key] = value
            return

        
        if len(self.lookup) == self.capacity:
            keys = set(self.lookup)
            i = len(self.q) - 1
            while i >= 0 and len(keys) > 1:
                if self.q[i] in keys:
                    keys.remove(self.q[i])
                i -= 1
            lru = keys.pop()
            del self.lookup[lru]
        
        self.lookup[key] = value
        return

