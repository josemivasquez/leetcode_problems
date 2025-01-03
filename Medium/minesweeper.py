class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> 
        List[List[str]]:
        v = set()
        target = board[click[0]][click[1]]
        if target == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        directions = []
        for i in range(-1, 1 + 1):
            for j in range(-1, 1 + 1):
                if i == 0 and j == 0: continue
                directions.append((i, j))
        
        mines = 0
        for d in directions:
            x = click[0] + d[0]
            y = click[1] + d[1]
            if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                continue
            if board[x][y] == 'M':
                mines += 1
        
        if mines > 0:
            board[click[0]][click[1]] = str(mines)
            return board

        board[click[0]][click[1]] = 'B'        
        for d in directions:
            x = click[0] + d[0]
            y = click[1] + d[1]
            if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                continue
            if board[x][y] != 'E':
                continue
            self.updateBoard(board, [x, y])
        
        return board
                
            


