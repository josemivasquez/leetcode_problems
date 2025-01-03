class Solution:
    def maximumSwap(self, num: int) -> int:
        ls = []
        while num > 0:
            d = num % 10
            ls.append(d)
            num = (num - d) // 10
        
        maxs = []
        m = ls[0]
        mindx = 0
        for i in range(1, len(ls)):
            e = ls[i]
            if e > m:
                m = e
                mindx = i
            maxs.append((m, mindx))
        
        i = len(ls) - 1
        while i > 0 and ls[i] >= maxs[i-1][0]:
            i -= 1
        if i != 0:            
            mindx = maxs[i-1][1]
            ls[i], ls[mindx] = ls[mindx], ls[i]

        num = 0
        order = 1
        for i in ls:
            num += i * order
            order *= 10
        return num

        

        


