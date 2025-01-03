"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        t = insertVal
        cn = head
        if head is None:
            n = Node(val=insertVal)
            n.next = n
            return n

        if t >= cn.val:
            ans = cn
            cn = cn.next
            while cn != head and cn.val >= ans.val and t >= cn.val:
                ans = cn
                cn = cn.next
            ans.next = Node(val=t, next=cn)

        elif t < cn.val:
            ans = cn
            cn = cn.next
            while cn != head and cn.val >= ans.val:
                ans = cn
                cn = cn.next
            # cn is the min, the "head"
            if t <= cn.val:
                ans.next = Node(val=t, next=cn)
            else:
                while t >= cn.val:
                    ans = cn
                    cn = cn.next
                ans.next = Node(val=t, next=cn)

        return head


            
