class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def getadj(pos):
            adj = []
            for d1, d2 in dirs:
                if 0 <= pos[0] + d1 < len(grid) and 0 <= pos[1] + d2 < len(grid[0]):
                    adj.append((pos[0] + d1, pos[1] + d2))
            return adj
                

        landindx = 2
        def land(grid, pos, indx):
            grid[pos[0]][pos[1]] = indx
            for i, j in getadj(pos):
                if grid[i][j] == "1":
                    land(grid, (i, j), indx)
        
        i = 0
        j = 0
        while i < len(grid):
            j = 0
            while j < len(grid[0]):
                if grid[i][j] == "1":
                    land(grid, (i, j), landindx)
                    landindx += 1
                j += 1
            i += 1
        
        return landindx - 2

                


