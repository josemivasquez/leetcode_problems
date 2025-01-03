class ProductOfNumbers:

    def __init__(self):
        self.ls = []
        

    def add(self, num: int) -> None:
        if num == 0:
            self.ls = []
        elif len(self.ls) == 0:
            self.ls = [num]
        else:
            self.ls.append(self.ls[-1] * num)
        

    def getProduct(self, k: int) -> int:
        if k > len(self.ls):
            return 0
        elif k == len(self.ls):
            return self.ls[-1]
        else:
            return int(self.ls[-1] / self.ls[len(self.ls) - 1 - k])
        
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
