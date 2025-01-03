class MovingAverage:

    def __init__(self, size: int):
        self.window = []
        self.windowsum = 0
        self.size = size

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.window.append(val)
            self.windowsum += val
            return self.windowsum / len(self.window)
        
        self.window.append(val)
        self.windowsum += val - self.window.pop(0)
        return self.windowsum / self.size

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
