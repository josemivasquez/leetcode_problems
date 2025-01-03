class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def ap1(grid):
            def group_size(pos, grid):
                if not 0 <= pos[0] < len(grid):
                    return 0
                if not 0 <= pos[1] < len(grid[0]):
                    return 0
                if grid[pos[0]][pos[1]] == 0:
                    return 0
                
                grid[pos[0]][pos[1]] = 0
                dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                r = 1
                for d in dr:
                    r += group_size([pos[0] + d[0], pos[1] + d[1]], grid)
                return r

                
            gmax = 0
            i1 = 0
            for r in grid:
                i2 = 0
                for e in r:
                    if e == 1:
                        gmax = max(gmax, group_size([i1, i2], grid))
                    i2 += 1
                i1 += 1
            
            return gmax

        def ap2(grid):
            rows = []
            grw = []
            grcode = 0
            indx = 0
            crs = None
            for c in grid[0]:
                if c == 1:
                    if crs is None: 
                        crs = indx
                else:
                    if crs is not None:
                        rows.append([crs, indx-1, grcode])
                        grcode += 1
                        grw.append(indx - crs)
                        crs = None
                indx += 1

            if crs is not None:
                rows.append([crs, indx-1, grcode])
                grcode += 1
                grw.append(indx - crs)
                crs = None

            
            nrows = []
            gridindx = 0
            for gridrow in grid[1:]:
                crs = None
                indx = 0
                for c in gridrow:
                    if c == 1:
                        if crs is None: 
                            crs = indx
                    else:
                        if crs is not None:
                            nrows.append([crs, indx-1, None])
                            crs = None
                    indx += 1
                if crs is not None:
                    nrows.append([crs, indx-1, None])
                    crs = None

                
                indx1 = 0
                indx2 = 0
                end = False

                if len(nrows) == 0:
                    rows.clear()
                    nrows, rows = rows, nrows
                    continue

                while True:
                    if indx1 == len(rows): end = True
                    else: r1 = rows[indx1]
                    
                    if indx2 == len(nrows): end = True
                    else: r2 = nrows[indx2]

                    if end: break

                    l, r = r1, r2
                    if r2[0] < r1[0]:
                        l, r = r, l
                    
                    if r[0] <= l[1]:
                        # Intersection
                        if r2[2] is None:
                            r2[2] = r1[2]
                            grw[r1[2]] += r2[1] - r2[0] + 1
                        elif r1[2] == r2[2]:
                            pass
                        else:
                            grw[r2[2]] += grw[r1[2]]
                            grw[r1[2]] = -1
                            r1[2] = r2[2]
                            

                    if r1[1] < r2[1]: 
                        indx1 += 1
                        continue
                    
                    if r2[2] is None:
                        # New Group
                        grw.append(r2[1] - r2[0] + 1)
                        r2[2] = grcode
                        grcode += 1
                    
                    indx2 += 1
                    
                    if r1[1] == r2[1]:
                        indx1 += 1
                
                if r2[2] is None:
                    # New Group
                    r2 = nrows[indx2]
                    grw.append(r2[1] - r2[0] + 1)
                    r2[2] = grcode
                    grcode += 1
                
                indx2 += 1
                while indx2 < len(nrows):
                    # New Group
                    r2 = nrows[indx2]
                    grw.append(r2[1] - r2[0] + 1)
                    r2[2] = grcode
                    grcode += 1
                    indx2 += 1
                    

                rows.clear()
                nrows, rows = rows, nrows
                gridindx += 1

            if len(grw) == 0:
                return 0
            return max(grw)
            
        return ap1(grid)










