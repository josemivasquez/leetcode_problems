class Solution:
    def alienOrder(self, words: List[str]) -> str:
        class Node:
            def __init__(self, letter):
                self.letter = letter
                self.lt = []
        
        presents = set()
        for w in words:
            for l in w: presents.add(l)

        nodes = dict()
        for l in list(presents):
            nodes[l] = Node(letter=l)
        
        # Another understanding
        # for w in words:
        #     for i in range(len(w)-1):
        #         lnode = nodes[w[i]]
        #         gnode = nodes[w[i+1]]
        #         if lnode == gnode: continue
        #         if lnode not in gnode.lt:
        #             gnode.lt.append(lnode)
        
        i = 0
        while i < len(words) - 1:
            lessw = words[i]
            grtw = words[i+1]
            j = 0
            while j < len(lessw) and j < len(grtw) and lessw[j] == grtw[j]:
                j += 1
            if j == len(lessw):
                i += 1
                continue
            if j == len(grtw):
                return ''
            
            gnode = nodes[grtw[j]]
            lnode = nodes[lessw[j]]
            gnode.lt.append(lnode)
            i += 1

        r = ''
        visited = set()
        ins = set()
        for letter in nodes:
            if nodes[letter] in visited: continue
            s = [(nodes[letter], 0)]
            ins.add(nodes[letter])
            while len(s) > 0:
                cn, done = s.pop()
                while done < len(cn.lt):
                    if cn.lt[done] in ins:
                        return ''
                    if cn.lt[done] in visited:
                        done += 1
                        continue
                    break
                
                if done == len(cn.lt):
                    r += cn.letter
                    visited.add(cn)
                    ins.remove(cn)
                    continue
                
                s.append((cn, done+1))
                s.append((cn.lt[done], 0))
                ins.add(cn.lt[done])
        
        return r
        
        
