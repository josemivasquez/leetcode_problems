class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = []
        for i in range(n): adj.append([])
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        rvals = [None] * n
        ins = [False] * n

        s = [(0, 0)]
        ins[0] = True
        while len(s) > 0:
            cn, donechilds = s.pop()
            if donechilds < len(adj[cn]) and ins[adj[cn][donechilds]]:
                donechilds += 1
            if donechilds == len(adj[cn]):
                apple = hasApple[cn]
                path = 0
                for child in adj[cn]:
                    if ins[child]: continue
                    if rvals[child][0]:
                        apple = True
                        path += 2 + rvals[child][1]
                ins[cn] = False
                rvals[cn] = (apple, path)
                continue
            
            s.append((cn, donechilds + 1))
            s.append((adj[cn][donechilds], 0))
            ins[adj[cn][donechilds]] = True

        return rvals[0][1]
        

            

                    

                
            
            

            
            



