class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        ans = nums[0]
        for n in nums[1:]:
            missings = n - ans - 1
            k -= missings
            if k <= 0:
                return n - 1 + k
            ans = n
        
        return ans + k



