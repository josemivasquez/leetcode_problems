# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ls = [(root, 0)]
        ls2 = []
        d = dict()
        while len(ls) > 0:
            for i in ls:
                node, col = i
                if col in d:
                    d[col].append(node.val)
                else:
                    d[col] = [node.val]

                if node.left is not None:
                    ls2.append((node.left, col-1))
                if node.right is not None:
                    ls2.append((node.right, col+1))
            ls, ls2 = ls2, ls
            ls2.clear()

        itm = list(d.items())
        itm.sort()
        res = []
        for i in itm:
            res.append(i[1])
        return res

