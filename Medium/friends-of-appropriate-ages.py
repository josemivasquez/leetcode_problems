class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        r = 0
        i = 1
        j = 0
        # Less Strict
        while i < len(ages):
            while j < i and ages[j] <= (ages[i] / 2) + 7:
                j += 1
            r += i - j
            i += 1
        
        ans = None
        i = 0
        reps = 0
        while i < len(ages):
            if ages[i] == ans or ans is None:
                ans = ages[i]
                reps += 1
            
            else:
                if ans > 14:
                    r += reps * (reps - 1) // 2
                ans = ages[i]
                reps = 1
            i += 1
        
        if ans > 14:
            r += reps * (reps - 1) // 2
        return r

            
                

        
        return r
            


