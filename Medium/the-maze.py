class Solution:
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]
        ) -> bool:
        def rf(maze, pi, pj, visited, dsti, dstj) -> bool:
            directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            visited.add((pi, pj))
            for d in directions:
                i = pi; j = pj
                while maze[i+d[0]][j+d[1]] == 0:
                    i += d[0]
                    j += d[1]
                if i == pi and j == pj:
                    continue
                if (i, j) in visited: continue
                if i == dsti and j == dstj: return True
                if rf(maze, i, j, visited, dsti, dstj): return True

            return False

        if destination[0] == start[0] and destination[1] == start[1]:
            return True

        border_maze = []
        nr = []
        for i in range(len(maze[0]) + 2): nr.append(1)
        border_maze.append(nr)
        for r in maze:
            nr = []
            nr.append(1)
            nr.extend(r)
            nr.append(1)
            border_maze.append(nr)
        nr = []
        for i in range(len(maze[0]) + 2): nr.append(1)
        border_maze.append(nr)
        
        dsti = destination[0] + 1
        dstj = destination[1] + 1
        visited = set()
        return rf(border_maze, start[0]+1, start[1]+1, visited, dsti, dstj)
