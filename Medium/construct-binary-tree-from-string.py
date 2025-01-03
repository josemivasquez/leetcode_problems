# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def readnum(self, s, i):
        n = ''
        indx = 0
        while indx < len(s) and (s[indx].isdigit() or s[indx] == '-'):
            n += s[indx]
            indx += 1
        
        return n, indx
    
        
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def rf(s):
            if len(s) == 0:
                return None

            v, indx = self.readnum(s, 0)
            endnum = indx
            root = TreeNode(val=int(v))
            
            if indx == len(s):
                # No childrens
                return root

            # At least one child
            # It must be left child, at least ()
            assert s[indx] == '('
            indx += 1
            lstr = ''
            p = 1
            while indx < len(s) and p > 0:
                if s[indx] == '(':
                    p += 1 
                elif s[indx] == ')':
                    p -= 1
                indx += 1
            
            # Readed left child
            ltree = rf(s[endnum+1:indx-1])
            root.left = ltree
            if indx == len(s):
                return root

            rtree = rf(s[indx+1: len(s)-1])
            root.right = rtree

            return root
        
        return rf(s)

            





