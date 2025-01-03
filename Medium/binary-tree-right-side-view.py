# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ls = [root]
        ls2 = []
        res = []

        if root is None:
            return []

        while len(ls) > 0:
            res.append(ls[-1].val)
            for n in ls:
                if n.left is not None:
                    ls2.append(n.left)
                if n.right is not None:
                    ls2.append(n.right)
            
            ls2, ls = ls, ls2
            ls2.clear()
        
        return res

