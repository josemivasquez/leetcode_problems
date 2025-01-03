class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = []
        self.cols = []

        for i in range(n):
            self.rows.append([0, 0])
            self.cols.append([0, 0])
        
        self.d1 = [0, 0]
        self.d2 = [0, 0]


    def move(self, row: int, col: int, player: int) -> int:
        player -= 1
        self.rows[row][player] += 1
        if self.rows[row][player] == self.n:
            return player + 1
        self.cols[col][player] += 1
        if self.cols[col][player] == self.n:
            return player + 1
        
        if row == col:
            self.d1[player] += 1
            if self.d1[player] == self.n:
                return player + 1
        if row + col == self.n - 1:
            self.d2[player] += 1
            if self.d2[player] == self.n:
                return player + 1
        
        return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
