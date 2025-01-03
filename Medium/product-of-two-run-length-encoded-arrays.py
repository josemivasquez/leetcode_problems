class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> 
        List[List[int]]:
        indx1 = 0
        indx2 = 0

        p1 = encoded1[indx1]
        p2 = encoded2[indx2]
        n1, r1 = p1
        n2, r2 = p2

        response = []
        jump1 = False
        jump2 = False

        ansn = ""
        while True:
            if jump1:
                indx1 += 1
                if indx1 == len(encoded1): break
                p1 = encoded1[indx1]
                jump1 = False
                n1, r1 = p1
            
            if jump2:
                indx2 += 1
                if indx2 == len(encoded2): break
                p2 = encoded2[indx2]
                jump2 = False
                n2, r2 = p2

            d = min(r1, r2)
            r1 -= d
            r2 -= d
            
            currentn = n1 * n2
            if currentn == ansn:
                response[-1][1] += d
            else:
                response.append([currentn, d])
                ansn = currentn

            if r1 == 0:
                jump1 = True
            if r2 == 0:
                jump2 = True
        
        return response






