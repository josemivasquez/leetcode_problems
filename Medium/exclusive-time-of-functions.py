class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ls = []
        for l in logs:
            func = ''
            i = 0
            while l[i] != ':':
                func += l[i]
                i += 1
            i += 1
            start = ''
            while l[i] != ':':
                start += l[i]
                i += 1
            if start == 'start':
                start = 0
            else:
                start = 1
            i += 1
            time = ''
            while i < len(l):
                time += l[i]
                i += 1
            ls.append((int(func), start, int(time)))
        
        # ls.sort(key=lambda x: (x[2], x[1]))
        
        r = [0] * n
        ans = ls[0][2]
        current = ls[0][0]
        stack = [current]
        for func, start, time in ls[1:]:
            if start == 0:
                if len(stack) > 0:
                    current = stack[-1]
                    r[current] += time - ans
                stack.append(func)
                ans = time
            else:
                current = stack.pop()
                r[current] += time - ans + 1
                ans = time + 1
        
        return r

            





                

