from random import randint
from heapq import heappushpop, heappush, heappop
class RandomizedCollection:

    def __init__(self):
        self.ls = []
        self.occ = dict()
        self.occs = dict()

    def insert(self, val: int) -> bool:
        # present = val in self.occs
        # if present:
        #     self.occs[val].add(len(self.ls))
        # else:
        #     s = set()
        #     s.add(len(self.ls))
        #     self.occs[val] = s
        
        # self.ls.append(val)
        # return not present

        # 2 AP
        present = val in self.occ
        if present:
            heappush(self.occ[val], -len(self.ls))
        else:
            self.occ[val] = [-len(self.ls)]
        self.ls.append(val)
        return not present

    def remove(self, val: int) -> bool:
        # if val not in self.occs:
        #     return False
        
        # victimindx = self.occs[val].pop()
        # if len(self.occs[val]) == 0:
        #     del self.occs[val]
        # lastindx = len(self.ls) - 1
        # lastval = self.ls[lastindx]
        # if victimindx == lastindx:
        #     self.ls.pop()
        #     return True
        
        # self.ls[victimindx] = lastval
        # # The thing O(1) ??
        # self.occs[lastval].remove(lastindx)
        # #
        # self.occs[lastval].add(victimindx)
        # self.ls.pop()
        # return True

        # 2 AP
        if val not in self.occ:
            return False
        
        victimindx = -heappop(self.occ[val])
        if len(self.occ[val]) == 0:
            del self.occ[val]
        
        if victimindx == len(self.ls) - 1:
            self.ls.pop()
            return True
        
        self.ls[victimindx] = self.ls[len(self.ls) - 1]
        lastval = self.ls.pop()
        heappop(self.occ[lastval])
        heappush(self.occ[lastval], -victimindx)

        return True

    def getRandom(self) -> int:
        return self.ls[randint(0, len(self.ls)-1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
