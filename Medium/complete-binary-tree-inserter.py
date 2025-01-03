# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        # Current parent of the last complete level
        self.root = root
        self.cpindx = None
        ls = [root]
        ls2 = []
        done = False
        while True:
            for i, n in enumerate(ls):
                if n.left is None or n.right is None:
                    self.cpindx = i
                    if n.left is not None:
                        ls2.append(n.left)
                    done = True
                    break
                else:
                    ls2.append(n.left)
                    ls2.append(n.right)
            
            if done:
                break

            ls, ls2 = ls2, ls
            ls2.clear()
        
        self.ls = ls
        self.ls2 = ls2
        
    def insert(self, val: int) -> int:
        n = TreeNode(val=val)
        cp = self.ls[self.cpindx]
        if cp.left is None:
            cp.left = n
            self.ls2.append(n)
            return cp.val
        
        cp.right = n
        self.ls2.append(n)
        r = cp.val
        if self.cpindx < len(self.ls) - 1:
            self.cpindx += 1
            return r
        
        self.ls, self.ls2 = self.ls2, self.ls
        self.ls2.clear()
        self.cpindx = 0
        return r

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
