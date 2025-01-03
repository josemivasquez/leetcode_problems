class SparseVector:
    def __init__(self, nums: List[int]):
        self.v = []
        zeros = 0
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                if zeros != 0:
                    self.v.append((False, zeros))
                    zeros = 0
                self.v.append((True, n))
        
        if zeros != 0:
            self.v.append((False, zeros))
            zeros = 0

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i1 = 0; i2 = 0
        p = 0
        a = self.v
        b = vec.v
        isnumber1, n1 = self.v[i1]
        isnumber2, n2 = vec.v[i2]
        jump1 = False; jump2 = False

        while True:
            if jump1:
                i1 += 1
                if i1 == len(self.v): break
                isnumber1, n1 = self.v[i1]
                jump1 = False
            if jump2:
                i2 += 1
                if i2 == len(vec.v): break
                isnumber2, n2 = vec.v[i2]
                jump2 = False

            if not isnumber1 and n1 == 0:
                jump1 = True; continue
            if not isnumber2 and n2 == 0:
                jump2 = True; continue
            
            if isnumber1 and isnumber2:
                p += n1 * n2
                jump1 = True; jump2 = True
            elif not isnumber1 and not isnumber2:
                m = min(n1, n2)
                n1 -= m
                n2 -= m
            else:
                if isnumber1:
                    jump1 = True; n2 -= 1
                else:
                    jump2 = True; n1 -= 1
        
        return p

            



            






# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
