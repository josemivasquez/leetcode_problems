# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        def rf (root, s):
            if root.left is None and root.right is None:
                if root.val == s:
                    return [[root.val]]
                else:
                    return []
            
            res = []
            if root.left is not None:
                lpaths = rf(root.left, s-root.val)
                for p in lpaths:
                    res.append([root.val] + p)

            if root.right is not None:
                rpaths = rf(root.right, s-root.val)
                for p in rpaths:
                    res.append([root.val] + p)
            
            return res
        
        return rf(root, targetSum)

                
            
            
            

