class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def rf(s, i):
            if len(s[i:]) == 0: return True
            j = i
            while j < len(s):
                while j < len(s) and s[i:j+1] not in d: j += 1
                if j == len(s): break
                if j+1 in memo:
                    rfv = memo[j+1]
                else:
                    rfv = rf(s, j+1)
                    memo[j+1] = rfv
                if rfv:
                    return True
                j += 1
            
            return False
        
        memo = dict()
        d = set()
        for w in wordDict:
            d.add(w)
        
        return rf(s, 0)

