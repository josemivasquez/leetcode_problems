from random import randint

class RandomizedSet:

    def __init__(self):
        self.d = dict()
        self.ls = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        
        self.d[val] = len(self.ls)
        self.ls.append(val)
        return True
            
    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        
        indx = self.d[val]
        del self.d[val]
        if indx == len(self.ls) -1:
            self.ls.pop()
            return True

        lastval = self.ls[-1]
        self.d[lastval] = indx

        self.ls[indx] = lastval
        self.ls.pop()
        return True
        
    def getRandom(self) -> int:
        rand = randint(0, len(self.ls)-1)
        return self.ls[rand]


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
