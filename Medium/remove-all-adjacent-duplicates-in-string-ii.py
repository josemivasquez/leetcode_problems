class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ls = []
        ans = s[0]
        cnt = 1
        for i in s[1:]:
            if i == ans:
                cnt += 1
            else:
                ls.append([ans, cnt])
                cnt = 1
            ans = i
        ls.append([ans, cnt])

        indx = 0
        while indx < len(ls):
            g = ls[indx]
            # if g[1] < k:
            #     indx += 1
            #     continue
            
            g[1] = g[1] % k
            if g[1] != 0:
                indx += 1
                continue
            
            ls.pop(indx)
            if indx == len(ls):
                break
            g = ls[indx]
            if indx == 0:
                continue
            ansg = ls[indx-1]
            if g[0] != ansg[0]:
                continue
            gq = g[1]
            ls.pop(indx)
            indx -= 1
            ls[indx][1] += gq

            # indx += 1
        
        sres = ''
        for g in ls:
            lg, qg = g
            for i in range(qg): sres += lg
        
        return sres

            

            
            
            



        
