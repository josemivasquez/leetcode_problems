class Solution:

    def addOperators(self, num: str, target: int) -> List[str]:
        def l0(x):
            return len(x) > 1 and x[0] == '0'

        def rf(num, leftmul, target):
            res = []
            if leftmul * int(num) == target and not l0(num):
                res.append(num)
            if len(num) == 1:
                return res

            i = 1
            while i < len(num):
                lnum = num[:i]
                rnum = num[i:]

                if l0(lnum):
                    i += 1
                    continue
                # if len(rnum) > 1 and rnum[0] == '0':
                #     i += 1
                #     continue

                lnum = int(lnum)
                # Multiplication case
                exprs = rf(rnum, leftmul * lnum, target)
                for exp in exprs:
                    res.append( str(lnum) + '*' + exp)

                # Add case
                exprs = rf(rnum, 1, target - leftmul * lnum)
                for exp in exprs:
                    res.append( str(lnum) +  '+' + exp)

                # Minus case
                exprs = rf(rnum, -1, target - leftmul * lnum)
                for exp in exprs:
                    res.append( str(lnum) + '-' + exp)
                
                i += 1
            
            return res
        
        return rf(num, 1, target)

