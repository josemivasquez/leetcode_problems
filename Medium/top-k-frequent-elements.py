class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        items = list(d.items())
        items.sort(key=lambda x: x[1], reverse=True)
        return [it[0] for it in items[:k]]
