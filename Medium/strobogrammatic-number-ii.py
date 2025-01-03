class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        d = dict()
        d[0] = 0
        d[1] = 1
        d[6] = 9
        d[8] = 8
        d[9] = 6

        def rf(n, shallow):
            if n == 1:
                return ["0", "1", "8"]
            if n == 2:
                ls =  ["11","69","88","96"]
                if not shallow:
                    ls.append("00")
                return ls
            
            rfv = rf(n-2, False)
            r = []
            for n in rfv:
                for i in d:
                    if shallow and i == 0: continue
                    r.append(str(i) + n + str(d[i]))
            
            return r
        
        return rf(n, True)
            

