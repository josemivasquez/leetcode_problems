class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ls = []
        ce = fruits[0]
        ct = 1
        for e in fruits[1:]:
            if e == ce:
                ct += 1
            else:
                ls.append((ce, ct))
                ct = 1
                ce = e
        
        ls.append((ce, ct))
        maxg = 0
        indx = 0
        cg = 0
        while indx < len(ls):
            e1, q1 = ls[indx]
            if indx == len(ls) - 1:
                maxg = max(maxg, q1)
                break
            
            e2, q2 = ls[indx + 1]
            cg = q1 + q2
            i = indx + 2
            while i < len(ls) and (ls[i][0] == e1 or ls[i][0] == e2):
                cg += ls[i][1]
                i += 1
            
            maxg = max(maxg, cg)
            indx = i - 1

        return maxg


        




