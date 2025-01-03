# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def rf(root):
            if root.left is None and root.right is None:
                return [[1], root.val]
            
            if root.left is not None:
                lld, lsum = rf(root.left)
            else:
                lld, lsum = ([], 0)
            
            if root.right is not None:
                rld, rsum = rf(root.right)
            else:
                rld, rsum = ([], 0)
            
            plus = 0
            for i in range(len(lld)):
                plus += root.val * ( 10** lld[i] )
                lld[i] += 1
            for i in range(len(rld)):
                plus += root.val * (10 ** rld[i] )
                rld[i] += 1
            
            s = lsum + rsum + plus
            lld.extend(rld)
            return (lld, s)
        
        return rf(root)[1]
            




            
        
