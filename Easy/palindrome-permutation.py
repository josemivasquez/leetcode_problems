class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = dict()
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        odd = False
        for v in d.values():
            if v % 2 != 0:
                if odd: return False
                odd = True
        
        return True
