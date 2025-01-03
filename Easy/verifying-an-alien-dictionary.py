class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = dict()
        cnt = 0
        for i in order:
            d[i] = cnt
            cnt += 1
        
        ans = words[0]
        for w in words[1:]:
            i = 0
            nice = False
            while i < min(len(ans), len(w)):
                if d[ans[i]] > d[w[i]]:
                    return False
                if d[ans[i]] < d[w[i]]:
                    nice = True
                    break
                i += 1
            
            if not nice and len(ans) > len(w):
                return False
            ans = w

        return True

