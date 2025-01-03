class Node:
        def __init__(self, val=None):
            self.prev = None
            self.next = None
            self.val = val
class LRUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity

        self.nodes = dict()
        self.values = dict()
        
    def kickback(self, key):
        n = self.nodes[key]
        if n.next is None:
            # Is tail
            return
        formertail = self.tail
        self.tail = n
        if n.prev is None:
            # Is head
            self.head = self.head.next
        
        formertail.next = n
        if n.prev is not None:
            n.prev.next = n.next
        n.next.prev = n.prev
        
        n.prev = formertail
        n.next = None
        
    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        val = self.values[key]
        self.kickback(key)
        return val
    
    def get_list(self):
        ls = []
        cn = self.head
        while not cn is None:
            ls.append(cn.val)
            cn = cn.next
        return ls

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values[key] = value
            self.kickback(key)
            return

        # New node
        if len(self.values) == self.capacity:
            victim = self.head.val
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            if self.tail.val == victim:
                self.tail = None
            
            del self.values[victim]
            del self.nodes[victim]

        self.values[key] = value
        n = Node(val=key)
        self.nodes[key] = n
        if self.head is None:
            self.head = n; self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
