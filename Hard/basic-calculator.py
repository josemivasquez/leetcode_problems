class Solution:
    def calculate(self, s: str) -> int:
        r = 0
        minus = False
        i = 0
        
        st = []
        while i < len(s):
            if s[i] == ' ': 
                i += 1
                continue
            if s[i] == '-':
                i += 1
                while s[i] == ' ': i += 1
                if s[i] == '(':
                    minus = not minus
                    st.append('-')
                    i += 1

                else:
                    n = int(s[i])
                    i += 1
                    while i < len(s) and s[i].isdigit():
                        n = n * 10 + int(s[i])
                        i += 1
                    if minus:
                        r += n
                    else:
                        r -= n
            elif s[i] == '(':
                st.append('+')
                i += 1
            elif s[i] == ')':
                popped = st.pop()
                if popped == '-':
                    minus = not minus
                i += 1
            elif s[i] == '+':
                i += 1
                continue
            elif s[i].isdigit():
                n = int(s[i])
                i += 1
                while i < len(s) and s[i].isdigit():
                    n = n * 10 + int(s[i])
                    i += 1
                if minus:
                    r -= n
                else:
                    r += n
        
        return r




            
                
                
                

