class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = dict()
        def rf(arr, k, indx):
            if len(arr) == 0:
                return 0
            r = 0
            max_segment = 0
            for i in range(k):
                if i == len(arr):
                    break

                max_segment = max(max_segment, arr[i])

                if (indx + i + 1) in memo:
                    rfv = memo[indx + i + 1]
                else:
                    rfv = rf(arr[i+1:], k, indx + i + 1)
                    memo[indx + i + 1] = rfv
                
                r = max(r, max_segment * (i + 1) + rfv)
            return r
        
        return rf(arr, k, 0)

