# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 
        'TreeNode':
        def get_path(root, n):
            if root is None:
                return None
            
            if root == n:
                return [root]
            
            lp = get_path(root.left, n)
            if lp is not None:
                lp.insert(0, root)
                return lp
            
            rp = get_path(root.right, n)
            if rp is not None:
                rp.insert(0, root)
                return rp
            
            return None

        pp = get_path(root, p)
        qp = get_path(root, q)

        i = 0
        m = min(len(pp), len(qp))
        while i < m and pp[i] == qp[i]:
            i += 1
        
        return pp[i-1]
