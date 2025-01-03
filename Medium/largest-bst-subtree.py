# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def rf(root):
            if root.left is None:
                lholds = True
                lsize = 0
                lmin = root.val
                lmax = root.val
            else:
                lholds, lsize, lmin, lmax = rf(root.left)
                lholds = lholds and lmax < root.val

            if root.right is None:
                rholds = True
                rsize = 0
                rmin = root.val
                rmax = root.val
            else:
                rholds, rsize, rmin, rmax = rf(root.right)
                rholds = rholds and root.val < rmin
            
            if not lholds or not rholds:
                size = max(lsize, rsize)
                return (False, size, None, None)
            
            size = lsize + rsize + 1
            return (True, size, lmin, rmax)
            
        return rf(root)[1]
