# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def abs(x): return x if x >= 0 else -x
        
        r = abs(target - root.val)
        rval = root.val
        cn = root
        while cn != None:
            if cn.val == target:
                return cn.val
            newr = abs(cn.val - target)
            if newr < r or (newr == r and cn.val < rval):
                rval = cn.val
                r = abs(cn.val - target)
            elif cn.val < target:
                cn = cn.right
            else:
                cn = cn.left
        
        return rval

