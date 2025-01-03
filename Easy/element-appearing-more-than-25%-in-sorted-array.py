class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        occgoal = len(arr) / 4
        ans = arr[0]
        occ = 1
        i = 1
        while i < len(arr):
            if arr[i] == ans:
                occ += 1
                if occ > occgoal:
                    return arr[i]
            else:
                ans = arr[i]
                occ = 1
            i += 1
