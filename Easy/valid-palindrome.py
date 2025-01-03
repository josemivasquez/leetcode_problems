class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for i in s:
            i = i.lower()
            if not i.isdigit() and not ord('a') <= ord(i) <= ord('z'):
                continue
            s1 += i
        
        i = 0
        j = len(s1) - 1
        while i < j and s1[i] == s1[j]:
            i += 1
            j -= 1
        if i < j:
            return False
        return True


