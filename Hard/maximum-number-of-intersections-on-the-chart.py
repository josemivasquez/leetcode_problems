from heapq import heappush, heappop
from collections import defaultdict
from typing import List

class Solution:
    def maxIntersectionCount(self, y: List[int]) -> int:
        n2indx = defaultdict(list)
        for i, n in enumerate(y):
            n2indx[n].append(i)
        
        optim = 0
        ends = []       
        for cn in sorted(n2indx.keys()):
            # Update ends
            # a < x, b > x
            while ends and ends[0] == cn:
                heappop(ends)
            cnindxs = n2indx[cn]

            # Calc I (cn)
            optim = max(optim, len(ends) + len(cnindxs))

            # Update ends a <= x, b > x
            for indx in cnindxs:
                if indx > 0 and y[indx-1] > y[indx]: heappush(ends, y[indx-1])
                if indx < len(y) - 1 and y[indx+1] > y[indx]: heappush(ends, y[indx
                    +1])
            
            # Calc I (cn + 0.5)
            optim = max(optim, len(ends))

        return optim

