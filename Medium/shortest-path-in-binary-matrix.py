from heapq import heappush as push
from heapq import heappop as pop

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = []
        for i in range(-1, 2): 
            for j in range(-1, 2): 
                if i == 0 and j == 0: continue
                dirs.append((i, j))
        
        def getadj(i, j):
            adj = []
            for d1, d2 in dirs:
                n1 = d1 + i
                n2 = d2 + j
                if not( 0 <= n1 < len(grid) and 0 <= n2 < len(grid[0]) ): continue
                if grid[n1][n2] == 1: continue
                adj.append((n1, n2))
            
            return adj

        if grid[0][0] != 0: return -1
        if len(grid) == 1 and len(grid[0]) == 1: return 1
        
        goal = (len(grid)-1, len(grid[0])-1)
        l1 = [(0, 0)]
        l2 = []
        visited = set()
        level = 1
        while len(l1) > 0:
            for n in l1:
                for adj in getadj(*n):
                    if adj in visited: continue
                    visited.add(adj)
                    if adj == goal:
                        return level + 1
                    l2.append(adj)
            
            l1, l2 = l2, l1
            l2.clear()
            level += 1
        
        return -1

          










            





