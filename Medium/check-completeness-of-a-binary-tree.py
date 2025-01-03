# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        s = [root]
        ns = []
        last_level = False
        while not last_level:
            for i in s:
                ns.append(i.left)
                ns.append(i.right)

                if i.left is None or i.right is None:
                    last_level = True
            
            s.clear()
            s, ns = ns, s
        
        none_start = False
        for n in s:
            if n is None: 
                none_start = True
            if none_start and n is not None:
                return False
        
        for n in s:
            if n is None: continue
            if n.left is not None or n.right is not None:
                return False
        
        return True

