class Solution:
    def countSubstrings(self, s: str) -> int:
        i = 0
        r = 0
        while i < len(s):
            r += 1
            j = i + 1
            z = i - 1
            while j < len(s) and z >= 0 and s[j] == s[z]:
                z -= 1
                j += 1
                r += 1
            
            j = i + 1
            z = i
            while j < len(s) and z >= 0 and s[j] == s[z]:
                z -= 1
                j += 1
                r += 1

            i += 1
        
        return r
            

