from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        def get_way_until_the_end(x, rels):
            path = []
            cr = x
            while cr in rels:
                ncr = rels[cr].pop()
                if len(rels[cr]) == 0:
                    del rels[cr]
                path.append([cr, ncr])
                cr = ncr
            return path

        rels = dict()
        qs = dict()
        for i, j in pairs:
            qs[j] = 0
            qs[i] = 0
        for i, j in pairs:
            qs[i] -= 1
            qs[j] += 1
            if i not in rels:
                rels[i] = set([j])
            else:
                rels[i].add(j)

        
        b = None 
        e = None
        for n, q in qs.items():
            if q == 0:
                continue
            if q == 1:
                e = n
            elif q == -1:
                b = n
        
        if b is None:
            b = pairs[0][0]
            e = pairs[0][0]
        
        res = get_way_until_the_end(b, rels) 
        i = 0
        while i < len(res):
            if res[i][0] not in rels:
                i += 1
                continue
            cicle = get_way_until_the_end(res[i][0], rels)
            for p in reversed(cicle):
                res.insert(i, p)
            
            i += 1
        
        return res
        

            
