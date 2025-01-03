class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        def swapbit(n, b):
            onebit = 2 ** b
            if (n // onebit) % 2 == 0:
                return n + onebit
            else:
                return n - onebit
        
        

        bits = dict()
        cnt = 0
        for i in range(ord('a'), ord('j') + 1):
            bits[chr(i)] = cnt
            cnt += 1
        
        n = 0
        d = dict()
        d[n] = 1
        r = 0
        for l in word:
            n = swapbit(n, bits[l])
            # How many matches
            onebit = 1
            matches = 0
            
            if n in d:
                matches += d[n]
            for i in range(10):
                if swapbit(n, i) in d:
                    matches += d[swapbit(n, i)]
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
            
            r += matches
        
        return r


                




