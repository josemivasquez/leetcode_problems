class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s):
            i = 0
            r = ''
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                l = j - i
                r += str(l) + s[i]
                i = j
            return r
        
        r = '1'
        for i in range(n-1):
            r = rle(r)
        
        return r



                
