class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diags = []
        for i in range(len(mat) - 1 + len(mat[0]) - 1 + 1): diags.append([])

        for i, row in enumerate(mat):
            for j, e in enumerate(row):
                if (i + j) % 2 == 0:
                    # Up diagonal
                    diags[i+j].insert(0, e)
                else:
                    diags[i+j].append(e)
        
        res = []
        for r in diags:
            for e in r: res.append(e)
        
        return res
                


        d = 0
        res = []
        while d < len(mat):
            if d % 2 == 0:
                i = d
                j = 0
                while i >= 0: res.append(mat[i][j]); i -= 1; j += 1
            
            else:
                i = 0
                j = d
                while j >= 0: res.append(mat[i][j]); i += 1; j-= 1
            
            d += 1
        
        endup = len(mat) % 2 == 1
        d = 1
        while d < len(mat[0]):
            if d % 2 == 0 if endup else 1:
                i = len(mat) - 1
                j = d
                while j < len(mat[0]): res.append(mat[i][j]); i -= 1; j += 1

            else:
                i = d
                j = len(mat[0]) - 1
                while i < len(mat): res.append(mat[i][j]); i += 1; j -= 1

            d += 1

        return res
        



