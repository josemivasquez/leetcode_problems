class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binary(n):
            r = []
            while n > 0:
                r.append(0 if n % 2 == 0 else 1)
                n = n // 2
            return r
        
        if n == 0:
            return 1
        
        if n < 0:
            n = -n
            x = 1/x
        
        exps = [x]
        bins = binary(n)
        for i in range(len(bins) - 1):
            e = exps[-1] * exps[-1]
            exps.append(e)
        
        r = 1
        for i, b in enumerate(bins):
            if b == 1:
                r *= exps[i]
            
        return r
