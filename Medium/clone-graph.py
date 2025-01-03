"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        inited = [None] * 101
        new_node = Node()
        inited[node.val] = new_node
        orgstack = [node]
        tarstack = [new_node]

        while True:
            if len(orgstack) == 0:
                break
            ocn = orgstack.pop(0)
            tcn = tarstack.pop(0)
            
            tcn.val = ocn.val
            for on in ocn.neighbors:
                if inited[on.val] is not None:
                    tcn.neighbors.append(inited[on.val])
                else:
                    nn = Node()
                    tcn.neighbors.append(nn)
                    tarstack.append(nn)
                    orgstack.append(on)
                    inited[on.val] = nn
            
        return new_node

