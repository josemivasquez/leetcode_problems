from typing import List

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def domultiset(s):
            ms = dict()
            for i in s:
                if i not in ms:
                    ms[i] = 1
                else:
                    ms[i] += 1
            
            return ms

        def substract(m1, m2):
            # m1 affected
            # m1 - m2
            for l in m1:
                if l in m2:
                    m1[l] -= m2[l]
        
        def add(m1, m2):
            # m1 affected
            # m1 + m2
            for l in m1:
                if l in m2:
                    m1[l] += m2[l]
        
        def ms2str(ms):
            res = ''
            for l in sorted(ms.keys()):
                res += l
                if ms[l] <= 0:
                    res += '0'
                else:
                    res += str(ms[l])
            return res
        
        def doletters2ms(fms):
            letters2ms = dict()
            for ms in fms:
                for l in ms:
                    if l not in letters2ms:
                        letters2ms[l] = [ms]
                    else:
                        letters2ms[l].append(ms)
            return letters2ms


        tms = domultiset(target) 
        fms = [domultiset(s) for s in stickers]
        letters2ms = doletters2ms(fms)
        
        for l in tms:
            if l not in letters2ms:
                return -1
        
        memo = dict()

        def rf(tms, fms):
            solved = all([tms[l] <= 0 for l in tms])
            if solved:
                return 0
            
            minval = None
            for l in tms:
                if tms[l] <= 0: continue
                matchingms = letters2ms[l]
                
                for ms in matchingms:
                    substract(tms, ms)
                    tohash = ms2str(tms)
                    if tohash in memo:
                        rfv = memo[tohash]
                    else:
                        rfv = rf(tms, fms)
                        memo[tohash] = rfv
                    add(tms, ms)
                    
                    minval = min(minval, rfv) if minval is not None else rfv
            
            return minval + 1

        return rf(tms, fms)


