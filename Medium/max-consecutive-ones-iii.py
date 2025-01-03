class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones = []
        zeros = []
        i = 0
        while i < len(nums):
            cnt = 0
            while i < len(nums) and nums[i] == 0: i += 1; cnt += 1
            zeros.append(cnt)
            cnt = 0
            while i < len(nums) and nums[i] == 1: i += 1; cnt += 1
            ones.append(cnt)
        cnt = 0
        while i < len(nums) and nums[i] == 0: i += 1; cnt += 1
        zeros.append(cnt)
        
        if k >= sum(zeros):
            return len(nums)
        
        zeros.pop(0)
        
        i = 0
        j = 0
        r = 0
        cr = ones[0]
        ck = k
        while i < len(ones):
            while j < len(zeros) and ck >= zeros[j]:
                ck -= zeros[j]
                cr += zeros[j]
                j += 1
                if j == len(zeros): break
                cr += ones[j]
                
            r = max(r, cr + ck)
            if j == len(zeros):
                return r

            if i == j:
                i += 1
                j += 1
                cr = ones[j]
                ck = k
                continue

            cr -= ones[i]
            cr -= zeros[i]
            ck += zeros[i]
            i += 1
        
        return r
            




        
        

            







        

