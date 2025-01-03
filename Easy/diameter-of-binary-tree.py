# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def r(node):
            if node is None:
                return -1, -1

            len_path_l_prev, depth_l = r(node.left)
            len_path_r_prev, depth_r = r(node.right)
                        
            len_path = depth_l + depth_r + 2
            depth = max(depth_l, depth_r) + 1
            len_path = max(len_path_l_prev, len_path_r_prev, len_path)
            # len_path = max(root_len_path, len_path_l, len_path_r)

            return len_path, depth
        
        return r(root)[0]




        
