class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        n = ord('z') - ord('a') + 1
        d = dict()
        for s in strings:
            fingerp = ()
            ans = ord(s[0])
            for l in s:
                dif = ord(l) - ans
                if dif < 0:
                    dif += n
                fingerp += (dif,)
                ans = ord(l)
            if fingerp in d:
                d[fingerp].append(s)
            else:
                d[fingerp] = [s]
        
        return list(d.values())

