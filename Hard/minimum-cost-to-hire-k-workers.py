from heapq import heappush, heappushpop
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> 
        float:
        ratios = [(wage[i]/quality[i], i) for i in range(len(quality))]
        ratios.sort()

        pq = []
        pqsum = 0
        amount = 0
        opamount = None
        rans = 0
        for r, i in ratios:
            if len(pq) < k:
                heappush(pq, -quality[i])
                pqsum += quality[i]
                rans = r
                continue
            
            amount = pqsum * rans
            opamount = min(opamount, amount) if opamount is not None else amount
            
            pqsum += quality[i]
            popped = - heappushpop(pq, -quality[i])
            pqsum -= popped

            rans = r

        amount = pqsum * r
        opamount = min(opamount, amount) if opamount is not None else amount

        return opamount

            
