class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.lookup = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node: Node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.lookup: 
            curr = self.lookup[key]
            self._remove(curr)
            self._add_to_tail(curr)
            return curr.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            curr = self.lookup[key]
            curr.val = value
            self._remove(curr)
            self._add_to_tail(curr)
            return
        
        if len(self.lookup) == self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.lookup[lru.key]
        
        new = Node(key, value)
        self._add_to_tail(new)
        self.lookup[key] = new
        return