# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        t = traversal
        i = 0
        n = int(t[0])
        i += 1
        while i < len(t) and t[i] != '-': n = n * 10 + int(t[i]); i += 1
        root = TreeNode(val=n)
        s = [root]
        d = 0
        while i < len(traversal):
            cd = 0
            while t[i] == '-': i += 1; cd += 1
            val = int(t[i])
            i += 1
            while i < len(t) and t[i] != '-': val = val * 10 + int(t[i]); i += 1
            if cd > d:
                node = TreeNode(val=val)
                s[-1].left = node
                s.append(node)
            elif cd == d:
                node = TreeNode(val=val)
                s.pop()
                s[-1].right = node
                s.append(node)
            else:
                node = TreeNode(val = val)
                while cd <= d:
                    s.pop()
                    d -= 1
                s[-1].right = node
                s.append(node)
            d = cd
                
        return root






