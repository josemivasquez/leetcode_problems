class Solution:
    
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = dict()
        def rf(s, i, j):
            if j <= i:
                return 0

            if s[i] == s[j]:
                return rf(s, i+1, j-1)

            if (i+1, j) in memo:
                lrfv = memo[(i+1, j)]
            else:
                lrfv = rf(s, i+1, j)
                memo[(i+1, j)] = lrfv
            
            if (i, j-1) in memo:
                rrfv = memo[(i, j-1)]
            else:
                rrfv = rf(s, i, j-1)
                memo[(i, j-1)] = rrfv
            
            return min( 1 + lrfv, 1 + rrfv )
    
        return rf(s, 0, len(s) -1) <= k

