class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        rl = -1
        while i <= j:
            m = (i + j) // 2
            me = nums[m]
            if me < target:
                i = m + 1
            elif me > target:
                j = m - 1
            else:
                if m == 0 or nums[m-1] < me:
                    rl = m
                    break
                j = m - 1
        
        if j < i:
            return [-1, -1]
        
        i = 0
        j = len(nums) - 1
        rr = -1
        while i <= j:
            m = (i + j) // 2
            me = nums[m]
            if me < target:
                i = m + 1
            elif target < me:
                j = m - 1
            else:
                if m == (len(nums) - 1) or me < nums[m+1]:
                    rr = m
                    break
                i = m + 1
        
        return [rl, rr]
