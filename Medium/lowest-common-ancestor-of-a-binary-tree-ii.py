# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 
        'TreeNode':
        def r(root, p):
            if root is None:
                return None
            if root.val == p:
                return [root]
            lp = r(root.left, p) 
            if lp is not None:
                lp.insert(0, root)
                return lp
            
            rp = r(root.right, p)
            if rp is not None:
                rp.insert(0, root)
                return rp
            
            return None
            
        path1 = r(root, p.val)
        path2 = r(root, q.val)

        if path1 is None or path2 is None: return None

        i = 0
        while True:
            if i >= len(path1) or i >= len(path2) or path1[i] != path2[i]:
                return path1[i-1]
            i += 1

