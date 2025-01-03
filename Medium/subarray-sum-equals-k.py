# from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i = 1
        while i < len(nums):
            nums[i] += nums[i-1]
            i += 1
        
        d = dict()
        # d = defaultdict(lambda : 0)
        d[0] = 1
        r = 0
        for i in nums:
            # r += d[i - k]
            # d[i] += 1

            if (i - k) in d:
                r += d[i - k]
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            
        return r

