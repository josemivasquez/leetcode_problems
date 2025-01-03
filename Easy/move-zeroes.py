class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        passed = 0
        n = len(nums)
        while passed < n:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                passed += 1
            else:
                passed += 1
                i += 1
        


