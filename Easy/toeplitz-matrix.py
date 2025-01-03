class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d = dict()
        for i, row in enumerate(matrix):
            for j, e in enumerate(row):
                if (i - j) not in d:
                    d[i - j] = e
                else:
                    if d[i - j] != e:
                        return False
        
        return True

