class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def bsearch(l, n):
            i = 0
            j = len(l) - 1
            while i <= j:
                m = (i + j)//2
                if n < l[m]:
                    j = m - 1
                elif l[m] < n:
                    i = m + 1
                else:
                    return m
            # Remember
            return i
        
        def median(ls):
            l = len(ls)
            if l % 2 == 0:
                return (ls[l//2] + ls[l//2 - 1]) / 2
            else:
                return ls[l//2]
                
        
        r = []
        window = []
        i = 0
        while i < k:
            window.append(nums[i])
            i += 1
        window.sort()
        r.append(median(window))

        j = 0
        while i < len(nums):
            # Insert l[i], pop l[j]
            jindx = bsearch(window, nums[j])
            window.pop(jindx)
            iindx = bsearch(window, nums[i])
            window.insert(iindx, nums[i])
            r.append(median(window))
            i += 1
            j += 1
        
        return r



        



