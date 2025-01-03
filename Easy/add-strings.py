class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carrier = 0
        res = ''

        while i >= 0 or j >= 0:
            if i >= 0:
                d1 = num1[i]
                i -= 1
            else:
                d1 = 0
            
            if j >= 0:
                d2 = num2[j]
                j -= 1
            else:
                d2 = 0
            
            d = carrier + int(d1) + int(d2)
            if d >= 10:
                carrier = 1
                d -= 10
            else:
                carrier = 0
            
            res = str(d) + res
        
        if carrier == 1:
            res = '1' + res
        
        return res


