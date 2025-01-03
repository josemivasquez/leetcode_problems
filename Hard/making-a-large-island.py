class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def getadj(pos):
            adj = []
            for d1, d2 in dirs:
                if 0 <= pos[0] + d1 < len(grid) and 0 <= pos[1] + d2 < len(grid[0]):
                    adj.append((pos[0] + d1, pos[1] + d2))
            return adj
        
        def land(grid, pos, indx):
            size = 1
            grid[pos[0]][pos[1]] = indx
            for i, j in getadj(pos):
                if grid[i][j] == 1:
                    size += land(grid, (i, j), indx)
            return size

        landindx = 2
        i = 0
        j = 0
        sizes = dict()
        while i < len(grid):
            j = 0
            while j < len(grid[0]):
                if grid[i][j] == 1:
                    size = land(grid, (i, j), landindx)
                    sizes[landindx] = size
                    landindx += 1
                j += 1
            i += 1
        
        if len(sizes) == 0:
            return 1
        
        r = max(sizes.values())
        i = 0
        while i < len(grid):
            j = 0
            while j < len(grid[0]):
                if grid[i][j] != 0: j += 1; continue
                adjislands = set()
                for a1, a2 in getadj((i, j)):
                    if grid[a1][a2] != 0:
                        adjislands.add(grid[a1][a2])
                cr = 0
                for island in list(adjislands):
                    cr += sizes[island]
                r = max(cr+1, r)
                
                j += 1
            i += 1
        
        return r
                        





        
        
