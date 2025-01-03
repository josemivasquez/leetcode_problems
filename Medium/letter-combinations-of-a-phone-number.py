class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = dict()
        letter = 'a'
        for n in range(2, 10):
            hm[n] = ''
            for i in range(3):
                hm[n] += letter
                letter = chr(ord(letter) + 1)
            if n == 7:
                hm[n] += letter
                letter = chr(ord(letter) + 1)


        
        hm[9] += 'z'

        if digits == "":
            return []
        
        def rf(digits):
            if len(digits) == 1:
                return [l for l in hm[int(digits[0])]]
            rfv = rf(digits[1:])
            res = []
            for s in rfv:
                for l in hm[int(digits[0])]:
                    res.append(l + s)
            
            return res
        
        return rf(digits)


            
