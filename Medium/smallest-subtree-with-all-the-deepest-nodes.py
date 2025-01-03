# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def rf(root):
            if root is None:
                return (-1, None)
            
            lmd, lnode = rf(root.left)
            rmd, rnode = rf(root.right)

            if lmd == rmd:
                return (lmd + 1, root)
            
            if lmd < rmd:
                return (rmd + 1, rnode)
            
            else:
                return (lmd + 1, lnode)
        
        return rf(root)[1]

