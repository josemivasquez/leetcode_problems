# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def getlb(root):
            if root.left is None:
                return []
            cn = root.left
            r = []
            while True:
                if cn.left is not None:
                    r.append(cn.val)
                    cn = cn.left
                elif cn.right is not None:
                    r.append(cn.val)
                    cn = cn.right
                else:
                    break
            
            return r
        
        def getrb(root):
            if root.right is None:
                return []
            
            cn = root.right
            r = []
            while True:
                if cn.right is not None:
                    r.append(cn.val)
                    cn = cn.right
                elif cn.left is not None:
                    r.append(cn.val)
                    cn = cn.left
                else:
                    break
            return r
        
        def getleaves(root):
            s = [(root, False)]
            r = []
            while len(s) > 0:
                cn, done = s.pop()
                if cn is None:
                    continue
                if done:
                    if cn.left is None and cn.right is None:
                        r.append(cn.val)
                    continue
                s.append((cn.right, False))
                s.append((cn, True))
                s.append((cn.left, False))
            return r
        if root.left is None and root.right is None:
            return [root.val]
        lb = getlb(root)
        rb = getrb(root)
        leaves = getleaves(root)
        i = 0
        j = len(rb) - 1
        while i < j:
            rb[i], rb[j] = rb[j], rb[i]
            i += 1
            j -= 1
        
        lb.insert(0, root.val)
        return lb + leaves + rb



                
                
            
                





        

