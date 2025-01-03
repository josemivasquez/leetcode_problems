class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def ignorei(s, i):
            return s[:i] + s[i+1:]

        def get_childs(st):
            res = []
            ans = None
            indx = 0
            for i in st:
                if i == '(' and ans != '(':
                    res.append(ignorei(st, indx))
                elif i == ')' and ans != ')':
                    res.append(ignorei(st, indx))

                ans = i
                indx += 1
            
            return res
        
        def is_valid(s):
            c = 0
            for i in s:
                if i == '(':
                    c -= 1
                elif i == ')':
                    c += 1
                if c > 0:
                    return False
            
            return c == 0

        if is_valid(s):
            return [s]
        ls = [s]
        ls2 = []
        while True:
            for st in ls:
                ls2.extend( get_childs(st) )
            
            ls2 = list(set(ls2))
            ls.clear()
            ls, ls2 = ls2, ls
            valids = []
            for st in ls:
                if is_valid(st):
                    valids.append(st)
            
            if len(valids) > 0:
                return valids
        
