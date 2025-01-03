from random import choice

class Solution:

    def __init__(self, nums: List[int]):
        self.d = dict()
        for i, n in enumerate(nums):
            if n in self.d:
                self.d[n].append(i)
            else:
                self.d[n] = [i]
        
    def pick(self, target: int) -> int:
        indxs = self.d[target]
        return choice(indxs)

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
