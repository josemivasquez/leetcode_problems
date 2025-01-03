class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        i = 1
        while i < len(arr): arr[i] += arr[i-1]; i += 1
        s = arr[-1]
        if s % 3 != 0:
            return False
        first = s // 3
        second = first * 2
        i = 0
        while i < len(arr) - 1 and arr[i] != first:
            i += 1
        if i == len(arr) - 1: return False
        i += 1
        while i < len(arr) - 1 and arr[i] != second:
            i += 1
        if i == len(arr) - 1:
            return False
        return True


