class Solution(object):

    def findShortestPath(self, master: 'GridMaster') -> int:
        freepos = set()
        # dfs discovery
        global cx
        global cy
        cx = 0
        cy = 0
        dirs = 'URDL'
        ndirs = { dr: i for i, dr in enumerate(dirs)}
        stack = [' U']
        target = None

        def nextpos(dir):
            if dir == 'U':
                return (cx -1 , cy)
            elif dir == 'D':
                return (cx + 1, cy)
            elif dir == 'L':
                return (cx, cy - 1)
            else:
                return (cx, cy + 1)
        def move(dir):
            global cx
            global cy
            npos = nextpos(dir)
            cx, cy = npos
            master.move(dir)
        def rev(dr):
            return dirs[(ndirs[dr] + 2) % 4]
        def nextdr(dr):
            ndr = ndirs[dr]
            if ndr == 3:
                return ' '
            else:
                return dirs[ndr + 1]
            
        while True:
            fromdr, todr = stack.pop()
            freepos.add( (cx, cy) )
            if master.isTarget():
                target = (cx, cy)
            if todr == ' ':
                if fromdr == ' ': break
                move(rev(fromdr))
                continue
            if master.canMove(todr) and nextpos(todr) not in freepos:
                stack.append(fromdr + nextdr(todr))
                move(todr)
                stack.append(todr + 'U')
            else:
                stack.append(fromdr + nextdr(todr))
        
        if target is None:
            return -1
        
        def getadj(pos):
            i, j = pos
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                yield (i + a, j + b)

        ls = [(0, 0)]
        ls2 = []
        distance = 0
        visited = set()
        visited.add((0, 0))
        while ls:
            for pos in ls:
                if pos == target:
                    return distance
                for adj in getadj(pos):
                    if adj not in freepos: continue
                    if adj in visited: continue
                    ls2.append(adj)
                    visited.add(adj)

            ls, ls2 = ls2, ls
            ls2.clear()
            distance += 1
        
        return -1
