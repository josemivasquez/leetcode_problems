class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def bsearch(arr, x):
            l = 0
            r = len(arr) - 1

            while True:
                if r < l:
                    return (r, l)

                m = (l + r) // 2
                if x == arr[m]:
                    return (m, m+1)
                elif x < arr[m]:
                    r = m -1
                else:
                    l = m +1
        def abs(x):
            return x if x > 0 else -x

        l, r = bsearch(arr, x)
        res = []
        while k > 0 and l >= 0 and r <= len(arr) - 1:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                res.insert(0, arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            k -= 1
        
        if k == 0:
            return res
        
        if l == -1:
            while k > 0:
                res.append(arr[r])
                r += 1
                k -= 1
        else:
            while k > 0:
                res.insert(0, arr[l])
                l -= 1
                k -= 1
        
        return res
        

                

        


