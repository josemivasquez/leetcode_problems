class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def testipv4(q):
            def isdigit(x): return x in {i for i in range(10)}
            i = 0
            for _ in range(3):
                x = ''
                while i < len(q) and q[i].isdigit(): x += q[i]; i += 1
                if i == len(q):
                    return False
                if len(x) == 0:
                    return False
                # Leading zeros
                if x[0] == '0' and x != '0':
                    return False
                xi = int(x)
                if not 0 <= xi <= 255:
                    return False
                if q[i] != '.':
                    return False
                i += 1
            
            x = ''
            while i < len(q) and q[i].isdigit(): x += q[i]; i += 1
            if i != len(q):
                return False
            # Leading zeros
            if len(x) == 0: return False
            if x[0] == '0' and x != '0':
                return False
            xi = int(x)
            if not 0 <= xi <= 255:
                return False
            

            return True

        def testipv6(q):
            def isdigit(x): return x in {i for i in range(10)}
            def ishexletter(x):
                return x in {'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 
                    'F'}
            i = 0
            for _ in range(7):
                x = ''
                while i < len(q) and (q[i].isdigit() or ishexletter(q[i])): x += q[i]
                    ; i += 1
                if not 1 <= len(x) <= 4:
                    return False
                if i == len(q): return False
                if q[i] != ':':
                    return False
                i += 1
            x = ''
            while i < len(q) and (q[i].isdigit() or ishexletter(q[i])): x += q[i]; i 
                += 1
            if i != len(q): return False

            # Leading zeros
            if len(x) == 0: return False
            if not 1 <= len(x) <= 4:
                return False
            
            return True
        
        if testipv4(queryIP):
            return "IPv4"
        if testipv6(queryIP):
            return "IPv6"
        return "Neither"
