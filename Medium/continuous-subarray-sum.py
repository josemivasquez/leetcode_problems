class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        def rf(ls):
            if len(ls) == 1:
                return False

            m = (0 + len(ls) - 1) // 2
            nextm = m + 1
            # blocks 0 .. m, m + 1 .. len(ls) - 1

            sums = set()
            i = m
            sm = 0
            while i >= 0:
                sm = (sm + ls[i]) % k
                sums.add(k - sm if sm != 0 else 0)
                i -= 1
            
            i = nextm
            sm = 0
            while i < len(ls):
                sm = (sm + ls[i]) % k
                if (sm % k) in sums:
                    return True
                i += 1
            
            ltrue = rf(ls[:m+1])
            if ltrue:
                return True
            rtrue = rf(ls[m+1:])
            if rtrue:
                return True
            
            return False
        
        def ap2(nums):
            rhm = dict()

            i = len(nums) -1
            s = 0
            while i >= 0:
                s = (s + nums[i]) % k
                if s not in rhm:
                    rhm[s] = i
                i -= 1
            rhm[0] = len(nums)
            allsum = s

            # -1 Iteration        
            if allsum in rhm and rhm[allsum] > 1:
                return True

            i = 0
            s = 0
            while i < len(nums) - 1:
                s = (s + nums[i]) % k
                tosearch = (allsum - s) % k
                if tosearch not in rhm:
                    i += 1
                    continue
                
                if rhm[tosearch] > i + 2:
                    return True

                i += 1
            
            return False
        
        def ap3(nums):
            prefixmod = 0
            modseen = dict()
            modseen[0] = -1

            for i, n in enumerate(nums):
                prefixmod = (prefixmod + n) % k
                if prefixmod in modseen:
                    leftindx = modseen[prefixmod]
                    if (leftindx + 1) < i:
                        return True
                else:
                    modseen[prefixmod] = i
            
            return False

        
        apr = 2
        if apr == 1:
            return rf(nums)
        elif apr == 2:
            return ap2(nums)
        elif apr == 3:
            return ap3(nums)


       



      
            


                








