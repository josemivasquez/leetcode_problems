from heapq import heappush as push
from heapq import heappushpop as pushpop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for i in range(k):
            push(q, nums[i])
        for e in nums[k:]:
            pushpop(q, e)
        return q[0]




        inq = set()
        i = 0
        while len(inq) < k and i < len(nums):
            if nums[i] not in inq:
                push(q, nums[i])
                inq.add(nums[i])
            i += 1

        while i < len(nums):
            if nums[i] not in inq:
                v = pushpop(q, nums[i])
                if v != nums[i]:
                    inq.remove(v)
                    inq.add(nums[i])
                
            i += 1
        
        return q[0]

        
