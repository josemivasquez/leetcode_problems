from copy import deepcopy
from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def getadj(pos):
            adj = []
            for d1, d2 in dirs:
                n1 = pos[0] + d1
                n2 = pos[1] + d2
                if 0 <= n1 < len(grid) and 0 <= n2 < len(grid[0]):
                    adj.append((n1, n2))
            
            return adj

        distances = deepcopy(grid)
        for l in distances:
            i = 0
            for e in l:
                if e != 0: l[i] = [None, None]
                else: l[i] = [0, 0]
                i += 1

        def expand(i, j):
            ls = [(i, j)]
            ls2 = []
            distance = 0
            visited = set()
            while len(ls) > 0:
                for pos in ls:
                    if pos in visited or (grid[pos[0]][pos[1]] != 0 and distance > 
                        0):
                        continue
                    visited.add(pos)
                    if distance > 0:
                        distances[pos[0]][pos[1]][0] += 1
                        distances[pos[0]][pos[1]][1] += distance
                    for adj in getadj(pos):
                        ls2.append(adj)
                distance += 1

                ls, ls2 = ls2, ls
                ls2.clear()

        ncities = 0  
        i = 0
        for l in grid:
            j = 0
            for e in l:
                if e == 1: 
                    expand(i, j)
                    ncities += 1
                j += 1
            i += 1

        mi = None
        mj = None
        m = None 
        i = 0
        for l in distances:
            j = 0
            for cities, totaldistance in l:
                if totaldistance is None: j += 1; continue
                if (m is None or totaldistance < m) and cities == ncities:
                    m = totaldistance
                    mi = i
                    mj = j
                j += 1 
            i += 1


