from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        def homo_sol(q, l):
            he = 1
            homostr = l[1] + l[0]
            response = ""
            while True:
                if he + 1 == len(q):
                    # All Homogeneus
                    response += homostr * q[he]
                    break
                
                d = q[he] - q[he + 1]
                response += homostr * d

                he += 1
                homostr = l[he] + homostr

            return response

        def to_homo(q, l):
            response = ""
            last_indx = len(q) - 1
            d = q[0] - q[1]

            while True:
                v = min(d, q[last_indx])
                response += (l[last_indx] + l[0]) * v

                q[0] -= v
                q[last_indx] -= v
                d -= v

                if q[last_indx] == 0:
                    q.pop()
                    l.pop()
                    last_indx -= 1
                
                if d == 0:
                    # Is homogeneus
                    return response, q, l

        if len(s) == 0: return ""
        if len(s) == 1: return s

        d = defaultdict(lambda : 0)
        for i in s: d[i] += 1

        items = list(d.items())
        items.sort(key=lambda x: x[1], reverse=True)
        frecs = []
        letters = []
        for l, f in items: letters.append(l); frecs.append(f)

        if frecs[0] - 1 > len(s) - frecs[0]:
            return ""
        
        response = ""
        if frecs[0] == frecs[1]:
            # Alredy homogeneus
            return homo_sol(frecs, letters)
        
        frecs[0] -= 1
        response = letters[0]
        if frecs[0] == frecs[1]:
            return response + homo_sol(frecs, letters)
        
        # Still not homo
        r, frecs, letters = to_homo(frecs, letters)
        response += r

        return response + homo_sol(frecs, letters)


    
        
    


