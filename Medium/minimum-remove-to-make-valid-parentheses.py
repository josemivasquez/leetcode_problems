class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def rf(s):
            if len(s) == 0:
                return ""
            opened = []
            i = 0
            while i < len(s):
                if s[i] != '(' and s[i] != ')': i += 1; continue
                if s[i] == ')':
                    if len(opened) == 0:
                        s.pop(i)
                    else:
                        opened.pop()
                        i += 1
                else:
                    opened.append(i)

            while len(opened) > 0:
                popped = opened.pop()
                s.pop(popped)
            
            return s

            # THE ANCIENT APPROACH
            i = 0
            j = len(s) - 1
            lr = ''
            while i < len(s):
                if s[i] == ')':
                    i += 1
                    
                elif s[i] != '(':
                    # letter
                    lr += s[i]
                    i += 1
                
                else:
                    break
            
            if i == len(s):
                return lr
            
            assert s[i] == '('
            
            rr = ''
            while j > i:
                if s[j] == '(':
                    j -= 1
                
                elif s[j] != ')':
                    # letter
                    rr = s[j] + rr
                    j -= 1

                else:
                    break
            
            if j == i:
                return lr + rr
            
            assert s[j] == ')'
            return lr + '(' + rf(s[i+1:j]) + ')' + rr
        
        p = 0
        r = ''
        for l in s:
            if l != '(' and l != ')':
                r += l
                continue
            
            if l == ')' and p == 0:
                continue
            
            if l == ')' and p > 0:
                p -= 1
                r += l
                continue
            
            if l == '(':
                r += l
                p += 1
                continue
        
        if p == 0:
            return r
        
        i = len(r) - 1
        r2 = ''
        while i >= 0:
            if r[i] == '(' and p > 0:
                i -= 1
                p -= 1
            
            else:
                r2 = r[i] + r2
                i -= 1
        
        return r2
            

            


        
        


            


            

