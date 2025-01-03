class Solution:
    def nextGreaterElement(self, n: int) -> int:
        def ls2num(ls):
            r = 0
            order = 1
            for i in reversed(ls):
                r += i * order
                order *= 10
            return r

        def num2ls(n):
            ls = []
            while n > 0:
                d = n % 10
                n = (n - d) // 10
                ls.insert(0, d)
            return ls

        ls = num2ls(n)
        endindx = len(ls) - 2
        while endindx >= 0 and ls[endindx] >= ls[endindx+1]:
            endindx -= 1
        
        if endindx == -1:
            return -1
        
        end = ls[endindx]
        upendindx = len(ls) - 1
        while ls[upendindx] <= end:
            upendindx -= 1
        
        ls[endindx], ls[upendindx] = ls[upendindx], ls[endindx]
        i = len(ls) - 1
        j = endindx + 1
        while i > j:
            ls[i], ls[j] = ls[j], ls[i]
            i -= 1
            j += 1
        
        r = ls2num(ls)
        if not r <= 2**31 - 1:
            return -1
        return r
        

