from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def rf(s):
            i = 0
            res = []
            while i < len(s):
                if s[:i+1] not in wordDict:
                    i += 1
                    continue
                if i + 1 == len(s):
                    res.append(s)
                    break
                for ws in rf(s[i+1:]):
                    res.append(s[:i+1] + ' ' + ws)
                i += 1
                
            return res

        return rf(s)

            
