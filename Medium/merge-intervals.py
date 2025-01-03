class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        response = []
        ci = intervals[0]
        for intv in intervals[1:]:
            if intv[0] <= ci[1]:
                # Merge
                ci[1] = max(intv[1], ci[1])
            else:
                # New ci
                response.append(ci)
                ci = intv

        response.append(ci)
        return response



