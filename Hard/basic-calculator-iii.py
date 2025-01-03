class Solution:
    def calculate(self, s: str) -> int:
        def div(a, b):
            if (a % b) == 0: return a // b
            if (a / b) < 0:
                return a // b + 1
            else:
                return a // b
            
        def eval_no_parenthesis(exp):
            nls = []
            opls = []
            i = 0
            while i < len(exp):
                n = 0
                minus = False
                if exp[i] == '-': minus = True; i += 1
                while i < len(exp) and exp[i].isdigit():
                    n = n * 10 + int(exp[i])
                    i += 1
                nls.append(n if not minus else -n)
                if i == len(exp): break
                opls.append(exp[i])
                i += 1
            
            i = 0
            while i < len(opls):
                if opls[i] == '/':
                    opls.pop(i)
                    a = nls.pop(i)
                    b = nls.pop(i)
                    nls.insert(i, div(a, b))
                elif opls[i] == '*':
                    opls.pop(i)
                    a = nls.pop(i)
                    b = nls.pop(i)
                    nls.insert(i, a * b)
                else:
                    i += 1
            
            i = 0
            while i < len(opls):
                op = opls.pop(i)
                a = nls.pop(0)
                b = nls.pop(0)
                if op == '+':
                    nls.insert(0,  a + b)
                else:
                    nls.insert(0, a - b)
            
            return nls[0]

        def eval(exp):
            i = 0
            r = ''
            while i < len(exp):
                while i < len(exp) and exp[i] != '(':
                    r += exp[i]
                    i += 1
                opened = 1
                if i == len(exp): break
                j = i + 1
                while opened != 0:
                    if exp[j] == '(': opened += 1
                    if exp[j] == ')': opened -= 1
                    j += 1

                n = eval(exp[i+1:j-1])
                r += str(n)
                i = j
            
            return eval_no_parenthesis(r)
        
        return eval(s)

            
            
