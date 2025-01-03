# from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def ap1(order, s):
            d = defaultdict(lambda: 0)
            indx = 0
            for i in order: 
                d[i] = indx
                indx += 1

            ss = sorted(s, key=lambda l: d[l])
            r = ""
            for l in ss: r += l
            return r
        
        def ap2(order, s):
            d = dict()
            for i, l in enumerate(order): d[l] = i

            m = []
            for i in range(len(order) + 1): m.append([])

            for l in s:
                if l not in d:
                    m[-1].append(l)
                else:
                    m[d[l]].append(l)
            

            resp = ""
            for ls in m:
                for l in ls:
                    resp += l

            return resp

        return ap2(order, s)      


            

        
