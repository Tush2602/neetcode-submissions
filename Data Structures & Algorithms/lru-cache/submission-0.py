class Node:
    def __init__(self, val : int, key=None):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

class LRUCache:

    def __init__(self, capacity : int):
        self.capacity = capacity
        self.left = Node(-1)
        self.right = Node(-1)

        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}
    
    def remove(self, node):
        node.next.prev, node.prev.next = node.prev, node.next

    def insert(self, node):
        node.prev = self.right.prev
        self.right.prev.next = node
        node.next = self.right
        self.right.prev = node

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

        self.cache[key] = Node(value, key)
        node = self.cache[key]
        self.insert(node)
        if len(self.cache) > self.capacity:
            rem_key = self.left.next.key
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[rem_key]
            

        

        
        
