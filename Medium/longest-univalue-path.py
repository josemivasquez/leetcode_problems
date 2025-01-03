# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def rf(root):
            if root.left is None:
                rl = 0
                lip = 0
            else:
                lrl, lrr, lip = rf(root.left)
                if root.val == root.left.val:
                    rl = max(lrl, lrr) + 1
                else:
                    rl = 0
            
            if root.right is None:
                rr = 0
                rip = 0
            else:
                rrl, rrr, rip = rf(root.right)
                if root.val == root.right.val:
                    rr = max(rrl, rrr) + 1
                else:
                    rr = 0
            
            maxpath = max(lip, rip, 1 + rl + rr)
            return (rl, rr, maxpath)
        
        return rf(root)[2] -1
            

