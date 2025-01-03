"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pp = []
        cn = p
        while cn != None:
            pp.insert(0, cn)
            cn = cn.parent
        
        qp = []
        cn = q
        while cn != None:
            qp.insert(0, cn)
            cn = cn.parent
        
        i = 0
        while i < len(pp) and i < len(qp) and pp[i] == qp[i]:
            i += 1
        
        return pp[i-1]
