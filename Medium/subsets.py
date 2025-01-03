class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def rf(nums):
            if len(nums) == 0:
                return [[]]
            rfv = rf(nums[1:])
            resp = []
            for s in rfv:
                ns = [nums[0]]
                for i in s: ns.append(i)
                resp.append(ns)
            
            resp.extend(rfv)
            
            return resp
        
        return rf(nums)




