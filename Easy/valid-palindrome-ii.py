class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        if not i < j:
            return True
        
        cuti = i
        cutj = j
        # Try cuti
        i = cuti + 1
        while i < j and s[i] == s[j]:
            i += 1; j -= 1
        if not i < j:
            return True
        
        # Try cutj
        i = cuti
        j = cutj - 1
        while i < j and s[i] == s[j]:
            i += 1; j -= 1
        if not i < j:
            return True
        
        return False
        

                
            
