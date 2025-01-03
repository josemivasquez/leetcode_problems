class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        indx = 0
        while indx < len(path):
            indx += 1
            if indx < len(path) and path[indx] == '/':
                indx += 1
            name = ''
            while indx < len(path) and path[indx] != '/':
                name += path[indx]
                indx += 1
            if name == '.' or name == '':
                continue
            if name == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(name)
        
        if len(stack) == 0:
            return '/'
        res = ''
        for i in stack:
            res += '/' + i
        return res
            
            
