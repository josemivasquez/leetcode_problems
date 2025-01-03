class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        instack = []
        done = []
        prereqs = []
        for i in range(numCourses):
            instack.append(False)
            done.append(False)
            prereqs.append([])
        
        for pr in prerequisites:
            a, b = pr
            prereqs[a].append(b)
        
        i = 0
        while i < numCourses:
            stack = [(i, 0)]
            instack[i] = True
            while len(stack) > 0:
                currcourse, presdone = stack.pop()
                if presdone == len(prereqs[currcourse]):
                    # Done
                    instack[currcourse] = False
                    done[currcourse] = True
                    continue
                
                stack.append((currcourse, presdone+1))
                nextpr = prereqs[currcourse][presdone]

                if instack[nextpr]:
                    return False
                if done[nextpr]:
                    continue

                instack[nextpr] = True
                stack.append((nextpr, 0))
            
            while i < numCourses and done[i]:
                i += 1
        
        return True

            



