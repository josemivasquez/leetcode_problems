class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diags = [[]]
        cnt = 0
        for i, row in enumerate(nums):
            for j, e in enumerate(row):
                if (i + j) > cnt:
                    diags.append([e])
                    cnt += 1
                else:
                    diags[i+j].append(e)
        
        res = []
        for diag in diags:
            for e in reversed(diag):
                res.append(e)
        
        return res




