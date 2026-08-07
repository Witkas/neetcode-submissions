class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.remaining_capacity = capacity
        self.cache = {}
        self.left = Node(None, None)
        self.right = Node(None, None)
        self.left.nxt, self.right.prev = self.right, self.left

    
    def remove(self, node):
        node.nxt.prev = node.prev
        node.prev.nxt = node.nxt
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.nxt = node
        nxt.prev = node
        node.prev, node.nxt = prev, nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            node.val = value
        else:
            self.cache[key] = Node(key, value)
            node = self.cache[key]
            if self.remaining_capacity > 0:
                self.remaining_capacity -= 1
            else:
                keyToRemove = self.left.nxt.key
                del self.cache[keyToRemove]
                self.remove(self.left.nxt)
            self.insert(node)
