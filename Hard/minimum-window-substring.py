class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = dict()
        for l in t:
            if l in target: target[l] += 1
            else: target[l] = 1
        completetarget = 0
        for n in target.values(): completetarget += n
        
        ms = dict()
        occr = []
        completed = 0
        i = 0
        # Have a solution
        while i < len(s) and completed < completetarget:
            l = s[i]
            if l not in target: i += 1; continue
            occr.append(i)
            if l not in ms:
                ms[l] = 1
                completed += 1
            else:    
                if ms[l] < target[l]:
                    completed += 1
                ms[l] += 1
            i += 1
        
        if completed < completetarget:
            return ""
        
        # Contract the solution
        while ms[s[occr[0]]] > target[s[occr[0]]]:
            poped = occr.pop(0)
            ms[s[poped]] -= 1

        
        r = s[occr[0]:i]
        rlen = i - occr[0]
        # Have another solutions
        while True:
            absent = s[occr.pop(0)]
            ms[absent] -= 1
            while i < len(s) and s[i] != absent:
                if s[i] not in target: i += 1; continue
                occr.append(i)
                ms[s[i]] += 1
                i += 1
            
            if i == len(s): return r
            occr.append(i)
            ms[s[i]] += 1
            i += 1

            # Contract the solution
            while ms[s[occr[0]]] > target[s[occr[0]]]:
                poped = occr.pop(0)
                ms[s[poped]] -= 1
            
            if (i - occr[0]) < rlen:
                rlen = i - occr[0]
                r = s[occr[0]:i]


            

            











        
            
