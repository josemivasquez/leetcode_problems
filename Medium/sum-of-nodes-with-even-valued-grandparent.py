# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def rf(root, parent, gp):
            if root is None:
                return 0

            lrfv = rf(root.left, root.val, parent)
            rrfv = rf(root.right, root.val, parent)
        
            if gp is not None and gp % 2 == 0:
                return lrfv + rrfv + root.val

            return lrfv + rrfv
        
        return rf(root, None, None)
