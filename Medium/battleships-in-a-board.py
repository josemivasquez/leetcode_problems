class Solution:
    

    def countBattleships(self, board: List[List[str]]) -> int:
        def delete_battleship(board, point):
            i1, i2 = point
            delta = []
            if i1 + 1 < len(board) and board[i1+1][i2] == 'X':
                delta = [1, 0]
            elif i2 + 1 < len(board[0]) and board[i1][i2+1] == 'X':
                delta = [0, 1]
            else:
                board[i1][i2] = '.'; return
            
            d1, d2 = delta
            while board[i1][i2] == 'X':
                board[i1][i2] = '.'
                i1 += d1; i2 += d2
                if i1 == len(board) or i2 == len(board[0]):
                    break

        response = 0
        for i1 in range(len(board)):
            for i2 in range(len(board[0])):
                if board[i1][i2] == 'X':
                    delete_battleship(board, (i1, i2))
                    response += 1
        
        return response
        

        
