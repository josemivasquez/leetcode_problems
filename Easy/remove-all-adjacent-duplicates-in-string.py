class Solution:
    def removeDuplicates(self, s: str) -> str:
        ls = []
        for i in s:
            ls.append(i)
        
        i = 0
        while i < len(ls) - 1:
            if ls[i] == ls[i+1]:
                ls.pop(i)
                ls.pop(i)
                if i > 0:
                    i -= 1
            else:
                i += 1
        
        s1 = ''
        for i in ls:
            s1 += i
        return s1


