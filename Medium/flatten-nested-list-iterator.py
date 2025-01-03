# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a 
    nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a 
    single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested 
    list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list_path = []
        self.indx_path = []
        self.ci = -1
        self.cl = nestedList
        self.r = self.inc()
    
    def inc(self):
        self.ci += 1
        while True:
            if not self.ci < len(self.cl):
                if len(self.indx_path) == 0:
                    return None
                else:
                    self.ci = self.indx_path.pop() + 1
                    self.cl = self.list_path.pop()
                continue
            
            if not self.cl[self.ci].isInteger():
                self.indx_path.append(self.ci)
                self.list_path.append(self.cl)
                self.cl = self.cl[self.ci].getList()
                self.ci = 0
                continue

            return self.cl[self.ci].getInteger()

    def next(self) -> int:
        response = self.r
        self.r = self.inc()
        return response

    def hasNext(self) -> bool:
        return not self.r is None
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
