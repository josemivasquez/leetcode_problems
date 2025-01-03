class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        h = heights
        r = []
        for i in h: r.append(0)
        s = [(h[0], 0)]
        i = 1
        while i < len(h):
            if h[i] < s[-1][0]:
                r[s[-1][1]] += 1
                s.append((h[i], i))
                i += 1
                continue
            
            while len(s) > 0 and h[i] >= s[-1][0]:
                r[s[-1][1]] += 1
                s.pop()
            if len(s) > 0:
                r[s[-1][1]] += 1
            s.append((h[i], i))
            i += 1
        
        return r

