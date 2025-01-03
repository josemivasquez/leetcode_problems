"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = 
        None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root is None:
            return ''
        s = [(root, False)]
        r = ''
        while len(s) > 0:
            cn, end = s.pop()
            if end:
                r += ')'
                continue
            
            r += '(' + str(cn.val)
            s.append((cn, True))
            for n in reversed(cn.children):
                s.append((n, False))
        
        return r
        
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        i = 0
        path = []
        root = None
        while i < len(data):
            if data[i] == '(':
                n = Node()
                if len(path) > 0:
                    path[-1].children.append(n)
                else:
                    root = n
                i += 1
                val = ''
                while data[i].isdigit(): 
                    val += data[i]; i += 1
                val = int(val)
                n.val = val
                path.append(n)
            else:
                path.pop()
                i += 1
        
        return root
                


                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
