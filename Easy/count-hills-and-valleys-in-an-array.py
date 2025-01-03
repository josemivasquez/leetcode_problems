class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums) and nums[i] == nums[0]:
            i += 1
        if i == len(nums):
            return 0
        if nums[0] < nums[i]:
            ansm = True
        else:
            ansm = False
        res = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i+1]:
                if not ansm:
                    res += 1
                ansm = True
            elif nums[i] > nums[i+1]:
                if ansm:
                    res += 1
                ansm = False
            i += 1

        return res
                


