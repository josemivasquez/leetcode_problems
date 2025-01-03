class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        ci = intervals[0]
        cnt = 0
        for intv in intervals[1:]:
            if ci[1] <= intv[0]:
                ci = intv
                continue
            
            if ci[1] < intv[1]:
                # Not Contains
                cnt += 1
            else:
                # Contains
                ci = intv
                cnt += 1
            
            
        

        return cnt
