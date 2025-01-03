class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        e = 0
        o = 0
        evenbit = 1
        while n > 0:
            d = n % 2
            if d == 1:
                if evenbit == 1:
                    e += 1
                else:
                    o += 1
            
            evenbit = 1 - evenbit
            n = (n - d) // 2
        
        return [e, o]

