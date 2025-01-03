class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ms = dict()
        for i in nums:
            if i not in ms: ms[i] = 1
            else: ms[i] += 1
        
        r = []
        # Triplicates
        if 0 in ms and ms[0] > 2:
            r.append((0, 0, 0))
        
        # Duplicates
        for n in ms:
            if n == 0: continue
            if ms[n] < 2: continue
            if -(n * 2) in ms:
                r.append((n, n, -(n*2)))
        
        # No duplicates
        keys = list(ms.keys())
        keys.sort()
        i = 0
        j = 0
        while i < len(keys) - 1:
            j = i + 1
            while j < len(keys):
                need = -(keys[i] + keys[j])
                if need <= keys[j]: j += 1; continue
                if need in ms:
                    r.append((keys[i], keys[j], need))
                j += 1
            i += 1
        
        return r
                



        

        
        
