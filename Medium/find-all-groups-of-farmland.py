class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        saw = []
        for r in land:
            l = []
            for i in r:
                l.append(None)
            saw.append(l)
        
        def findgroup(land, saw, i, j):
            x = i
            while x < len(land) and land[x][j] == 1:
                x += 1
            y = j
            while y < len(land[0]) and land[i][y] == 1:
                y += 1
            
            for a in range(i, x):
                for b in range(j, y):
                    saw[a][b] = 1
            
            return [i, j, x-1, y-1]
        
        resp = []
        for i, r in enumerate(land):
            for j, e in enumerate(r):
                if saw[i][j] is not None:
                    continue
                if land[i][j] == 1:
                    group = findgroup(land, saw, i, j)
                    resp.append(group)
        
        return resp


                



