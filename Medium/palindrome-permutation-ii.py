class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def rever(s):
            r = ''
            for i in reversed(s):
                r += i
            return r

        def rf(grl, grc):
            if len(grc) == 1:
                return [grl[0] * grc[0]]
            
            res = []
            i = 0
            while i < len(grl):
                l = grl[i]
                popped = False
                grc[i] -= 1
                if grc[i] == 0:
                    popped = True
                    grc.pop(i)
                    grl.pop(i)
                
                for s in rf(grl, grc):
                    res.append(l + s)
                
                if popped:
                    grc.insert(i, 1)
                    grl.insert(i, l)
                else:
                    grc[i] += 1

                i += 1
            
            return res
        
        d = dict()
        grl = []
        grc = []
        cnt = 0
        for i in s:
            if i in d:
                grc[d[i]] += 1
            else:
                grl.append(i)
                grc.append(1)
                d[i] = cnt
                cnt += 1
        
        seed = None
        i = 0
        while i < len(grl):
            if grc[i] % 2 == 1:
                if seed is not None:
                    return []
                else:
                    seed = grl[i]

            grc[i] = grc[i] // 2
            if grc[i] == 0:
                grc.pop(i)
                grl.pop(i)
            else:
                i += 1
            
        lperms = rf(grl, grc)
        if seed is not None and len(lperms) == 0:
            return [seed]
        for i in range(len(lperms)):
            if seed is not None:
                lperms[i] = lperms[i] + seed + rever(lperms[i])
            else:
                lperms[i] += rever(lperms[i])
        
        return lperms
                
                

