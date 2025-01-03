class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def verify(w, d, maxcap) -> Optional[int]:
            indx = 0
            current_charge = 0
            maxopt = 0
            left_days = d

            while left_days > 0 and indx < len(w):
                if current_charge + w[indx] > maxcap:
                    maxopt = max(maxopt, current_charge)
                    current_charge = 0
                    left_days -= 1
                    
                else:
                    current_charge += w[indx]
                    indx += 1
            
            if indx == len(w):
                return maxopt
            
            if left_days == 0:
                return None
        
        def fast_verify(w, d, c):
            indx = 0
            current_charge = 0
            left_days = d

            while left_days > 0 and indx < len(w):
                current_charge += w[indx]
                if current_charge > c:
                    current_charge = 0
                    left_days -= 1
                else:
                    indx += 1
            
            if indx < len(w):
                return False
            else:
                return True

        
        s = sum(weights)
        l = max(s//days + 0 if s % days == 0 else 1, max(weights))
        r = s

        while True:
            if l == r:
                return l
            m = (l + r) // 2
            opt = fast_verify(weights, days, m)
            if not opt:
                l = m + 1
            else:
                r = m

        mincap = max(sum(weights)/days, max(weights))
        current_charge = 0
        indx = 0
        for i, e in enumerate(weights):
            current_charge += e
            if current_charge > mincap:
                current_charge -= e
                indx = i
                break
        
        while True:
            mopt = verify(weights[indx:], days-1, current_charge + weights[indx] - 
                1)
            if mopt is not None:
                return mopt
            
            current_charge += weights[indx]
            indx += 1

        memo = dict()
        def rf(w, d, indx):
            mcap = sum(w) / d
            if len(w) == 0:
                return 0
            if d == 1:
                return sum(w)
            i = 0
            cap = 0
            while i < len(w) - 1:
                cap += w[i]
                if cap < mcap:
                    i += 1
                    continue
                if (indx+i+1, d-1) in memo:
                    rfv = memo[(indx+i+1, d-1)]
                else:
                    rfv = rf(w[i+1:], d-1, indx+i+1)
                    memo[(indx+i+1, d-1)] = rfv

                minr = rfv
                if minr < cap + w[i+1]:
                    return max(cap, minr)
                i += 1
            return cap + w[i]

        return rf(weights, days, 0)

