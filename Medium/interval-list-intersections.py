class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: 
        List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0: return []
        if len(secondList) == 0: return []
        intr1 = firstList[0]
        intr2 = secondList[0]
        jump1 = False; jump2 = False
        i1 = 0; i2 = 0
        response = []
        while True:
            if jump1:
                i1 += 1
                if i1 == len(firstList): break
                intr1 = firstList[i1]
                jump1 = False
            if jump2:
                i2 += 1
                if i2 == len(secondList): break
                intr2 = secondList[i2]
                jump2 = False

            s1, e1 = intr1
            s2, e2 = intr2
            
            # No intersection
            if s2 > e1: jump1 = True; continue
            elif s1 > e2: jump2 = True; continue

            intersection = (max(s1, s2), min(e1, e2))
            response.append(intersection)
            endintersection = intersection[1]
            if e1 == endintersection: jump1 = True
            if e2 == endintersection: jump2 = True
        
        return response
