class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for row in matrix:
            srow = 0
            for i, e in enumerate(row):
                row[i] += srow
                srow += e
        irow = 1
        for row in matrix[1:]:
            for i, e in enumerate(row):
                row[i] += matrix[irow-1][i]
            irow += 1
        
        self.matrix = matrix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        total = matrix[row2][col2]
        m = matrix[row1-1][col1-1] if row1-1 >= 0 and col1-1 >= 0 else 0
        up = matrix[row1-1][col2] if row1-1 >= 0 else 0 
        left = matrix[row2][col1-1] if col1-1 >= 0 else 0

        return total - m - (up - m) - (left - m)
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
