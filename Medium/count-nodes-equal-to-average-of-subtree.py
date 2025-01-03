# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def averageOfSubtree(self, root: TreeNode) -> int:
        def rf(node):
            if node is None:
                return 0, 0, 0

            w1, n1, r1 = rf(node.left)
            w2, n2, r2 = rf(node.right)

            w = w1 + w2 + node.val
            n = n1 + n2 + 1
            r = r1 + r2
            if node.val == int(w / n):
                r += 1
            
            return w, n, r

        return rf(root)[2]

        
