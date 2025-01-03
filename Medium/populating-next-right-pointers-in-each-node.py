"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 
        'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return None
        s = [root]
        ns = []
        while True:
            next_node = s[-1]
            next_node.next = None
            for n in reversed(s[:-1]):
                n.next = next_node
                next_node = n
            
            if s[0].left is None:
                return root

            for n in s:
                ns.append(n.left)
                ns.append(n.right)
            
            s.clear()
            s, ns = ns, s





