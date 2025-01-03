class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def r(l):
            mindx = len(l) // 2
            m = l[mindx]

            if not (mindx == 0 or l[mindx-1] < m):
                return r(l[:mindx])
            if not (mindx == len(l) - 1 or l[mindx+1] < m):
                return mindx + r(l[mindx+1:]) + 1
            
            return mindx
        
        return r(nums)



