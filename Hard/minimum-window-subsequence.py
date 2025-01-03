class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        if len(s2) == 1:
            if s2[0] in s1: return s2[0]
            else: return ""

        l2i = dict()
        r = ''
        rlen = None

        i = 0
        for l in s2:
            if l not in l2i:
                l2i[l] = [i]
            else:
                l2i[l].append(i)
            i += 1
        
        # The i has completed wi letters
        waiting = []
        for l in s2:
            waiting.append(None)
        
        i = 0
        for l in s1:
            if l not in l2i: i += 1; continue
            indxs = l2i[l]
            for indx in reversed(indxs):
                if indx == 0:
                    waiting[1] = i
                    continue
                
                if waiting[indx] == None:
                    continue
                if indx == len(waiting) - 1:
                    # Match
                    currlen = (i - waiting[indx] + 1)
                    
                    if rlen is None or currlen < rlen:
                        rlen = currlen
                        r = s1[waiting[indx]: i + 1]
                    waiting[indx] = None
                    continue

                waiting[indx + 1] = waiting[indx]
                waiting[indx] = None
            i += 1
        return r

            



        

        




