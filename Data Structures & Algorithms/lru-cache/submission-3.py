class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.length = capacity
        self.cache = {}  # Storing the cache

        # LRU and MRU
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    # insert at end
    def insert(self,node):
        mru = self.right.prev
        mru.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = mru
        return

    # remove from begenning
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None
        return

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) # Remove element from current position
            self.insert(self.cache[key]) # Add element to the MRU position
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.length:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)
        return
