class Solution:
    
    def isNumber(self, s: str) -> bool:
        def isdigit(ch):
            return ch in {str(i) for i in range(0, 10)}
        
        def read_digits(s):
            i = 0
            while True:
                if len(s) == i or not isdigit(s[i]):
                    return i, s[i:]
                i += 1
        
        def validate_exp(s):
            if s == "" or (s[0] != "E" and s[0] != 'e'): return False
            s = s[1:]
            if s == "": return False
            if s[0] == '+' or s[0] == '-': s = s[1:]
            n, s = read_digits(s)
            if n == 0:
                return False
            if s != '':
                return False
            return True

        # Validate integer or decimal
        # Int: -|+ digit+
        # Decimal: digit+. | .digit+ | digit+.digit+
        # SA P B E SC

        if s == "": return False
        if s[0] == '+' or s[0] == '-': s = s[1:]

        n, s = read_digits(s)
        digitsbeforedot = n > 0

        if s == '':
            return digitsbeforedot
        
        elif s[0] == 'E' or s[0] == 'e':
            if not digitsbeforedot: 
                return False
            else:
                return validate_exp(s)
        
        elif s[0] != '.':
            return False
        
        s = s[1:]
        n, s = read_digits(s)
        digitsafterdot = n > 0

        if not digitsafterdot and not digitsbeforedot:
            return False
        
        if s == "":
            return True
        
        else:
            return validate_exp(s)



