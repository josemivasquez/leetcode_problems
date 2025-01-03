class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        i = 0
        j = len(self.l) - 1
        while i <= j:
            m = (i + j) // 2
            if self.l[m] == num:
                i = m
                break
            elif num < self.l[m]:
                j = m - 1
            else:
                i = m + 1
        
        self.l.insert(i, num)

    def findMedian(self) -> float:
        l = len(self.l)
        if l % 2 == 0:
            return (self.l[l // 2] + self.l[l // 2 - 1]) / 2
        else:
            return self.l[l // 2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
