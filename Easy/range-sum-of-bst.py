# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def stree(root):
            if root is None:
                return 0
            return root.val + stree(root.left) + stree(root.right)
        
        def sbetter(root, val):
            if root is None:
                return 0
            if root.val == val:
                return root.val + stree(root.right)
            elif root.val < val:
                return sbetter(root.right, val)
            else:
                return root.val + stree(root.right) + sbetter(root.left, val)
        
        def slower(root, val):
            if root is None:
                return 0
            if root.val == val:
                return root.val + stree(root.left)
            elif root.val < val:
                return root.val + stree(root.left) + slower(root.right, val)
            else:
                return slower(root.left, val)
        
        def rf(root, l, h):
            if root is None:
                return 0
            if h < root.val:
                return rf(root.left, l, h)
            elif root.val < l:
                return rf(root.right, l, h)
            if root.val == h:
                return root.val + sbetter(root.left, l)
            elif root.val == l:
                return root.val + slower(root.right, h)
            else:
                return root.val + sbetter(root.left, l) + slower(root.right, h)
        
        return rf(root, low, high)
            


            

