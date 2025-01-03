class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = 0
        for n in arr:
            missings = n - ans - 1
            if missings >= k:
                return ans + k
            k -= missings
            ans = n
        return n + k
