class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()
        frontier = []
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def val(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        def rf(mt, pos, visited, frontier):
            i, j = pos
            f = False
            visited.add(pos)
            for d1, d2 in dirs:
                if not val(i+d1, j+d2): continue
                if (i+d1, j+d2) in visited: continue
                if mt[i+d1][j+d2] == 0:
                    f = True
                else:
                    rf(mt, (i+d1, j+d2), visited, frontier)
            
            if f:
                frontier.append(pos)
        
        done = False
        for i, l in enumerate(grid):
            for j, e in enumerate(l):
                if e == 1:
                    rf(grid, (i, j), visited, frontier)
                    done = True
                if done: break
            if done: break
        
        its = 0
        l2 = []
        while len(frontier) > 0:
            for i, j in frontier:
                for d1, d2 in dirs:
                    if not val(i+d1, j+d2): continue
                    if (i+d1, j+d2) in visited: continue
                    
                    if grid[i+d1][j+d2] == 1:
                        return its

                    visited.add((i+d1, j+d2))
                    l2.append((i+d1, j+d2))
                
            frontier, l2 = l2, frontier
            l2.clear()
            its += 1
    
        return None







