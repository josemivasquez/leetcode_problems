class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> 
        List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]
        r = []
        ans = lower
        if ans != nums[0]:
            r.append([ans, nums[0]-1])
        ans = nums[0]
        for n in nums[1:]:
            if ans == n or n == ans + 1:
                ans = n
                continue
            r.append([ans+1, n-1])
            ans = n
        
        if ans == upper:
            return r
        r.append([ans+1, upper])
        return r
            
