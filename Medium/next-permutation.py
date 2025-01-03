class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        indx = len(nums) - 1
        brindx = -1
        m = -1
        while indx >= 0:
            if nums[indx] >= m:
                m = nums[indx]
            else:
                brindx = indx
                break
            indx -= 1
        
        if brindx == -1:
            reverse(nums, 0, len(nums) - 1)            
            return nums
        
        br = nums[brindx]
        indx = len(nums) - 1
        replacebrindx = -1
        while indx >= 0:
            if nums[indx] > br:
                replacebrindx = indx
                break
            indx -= 1
        
        nums[brindx], nums[replacebrindx] = nums[replacebrindx], nums[brindx]
        reverse(nums, brindx + 1, len(nums) - 1)
        
        return nums




