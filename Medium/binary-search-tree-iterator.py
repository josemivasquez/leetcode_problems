# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.ls = []
        stack = [(root, False)]

        while len(stack) > 0:
            cn , fixed = stack.pop()
            if cn is None:
                continue
            if fixed:
                self.ls.append(cn.val)
                continue
            
            stack.append((cn.right, False))
            stack.append((cn, True))
            stack.append((cn.left, False))
        
        self.indx = 0
        
    def next(self) -> int:
        r = self.ls[self.indx]
        self.indx += 1
        return r
        
    def hasNext(self) -> bool:
        return self.indx != len(self.ls) 
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
