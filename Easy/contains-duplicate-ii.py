class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = i
                continue
            mindx = d[n]
            if (i - mindx) <= k:
                return True
            d[n] = i
        
