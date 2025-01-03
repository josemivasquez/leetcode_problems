# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mincol = 0
        maxcol = 0
        r = [[]]
        rrow = [[]]

        l1 = [(root, 0, 0)]
        l2 = []
        
        while True:
            for n, row, col in l1:
                if col < mincol:
                    r.insert(0, [])
                    rrow.insert(0, [])
                    mincol -= 1
                if maxcol < col:
                    r.append([])
                    rrow.append([])
                    maxcol += 1
                
                rrow[col - mincol].append(n.val)

                if n.left is not None:
                    l2.append((n.left, row + 1, col - 1))
                if n.right is not None:
                    l2.append((n.right, row + 1, col + 1))

            for i, l in enumerate(rrow):
                l.sort()
                r[i].extend(l)
                l.clear()
            
            l1, l2 = l2, l1
            l2.clear()
            if len(l1) == 0:
                break
        
        return r
            



            

                




