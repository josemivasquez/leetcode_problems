# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dnodes(root, d):
            if root is None: return []
            if d < 0: return []
            l1 = [root]
            l2 = []
            cd = 0
            while cd < d:
                for n in l1:
                    if n.left is not None: l2.append(n.left)
                    if n.right is not None: l2.append(n.right)
                l1, l2 = l2, l1
                l2.clear()
                cd += 1
            
            return [n.val for n in l1]
        
        def gpath(root, n):
            s = [(root, False)]
            path = []
            while len(s) > 0:
                cn, seen = s.pop()
                if cn is None: continue
                if cn == n:
                    return path + [cn]
                if not seen:
                    path.append(cn)
                    s.append((cn, True))
                    s.append((cn.left, False))
                    s.append((cn.right, False))
                else:
                    path.pop()
            
            return None
            
        path = gpath(root, target)
        if path is None:
            return []
        lpath = len(path)
        i = 0
        r = []
        while i < len(path) - 1:
            n = path[i]
            d = lpath - i - 1
            if d > k:
                i += 1
                continue
            if d == k:
                i += 1
                r.append(n.val)
                continue
            if path[i+1] == path[i].left:
                r.extend(dnodes(path[i].right, k - d - 1))
            if path[i+1] == path[i].right:
                r.extend(dnodes(path[i].left, k - d - 1))
            i += 1
        
        r.extend(dnodes(target, k))

        return r

            
                


            
            
            

            

                

        

            



