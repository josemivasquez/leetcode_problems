class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) == 0:
            return []

        maxr = heights[-1]
        res = [len(heights) - 1]
        indx = len(heights) - 2
        while indx >= 0:
            h = heights[indx]
            if h > maxr:
                res.insert(0, indx)
                maxr = h
            indx -= 1
        
        return res
            

