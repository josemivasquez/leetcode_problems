class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        r = 0
        p = 0
        for i, l in enumerate(s):
            if p == 0 and l == ')':
                r += 1
            elif p > 0 and l == ')':
                p -= 1
            elif l == '(':
                p += 1
        
        r += p
        return r
