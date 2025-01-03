class RangeModule:

    def __init__(self):
        self.ls = []

    def getindx(self, l):
        ls = self.ls    
        i = 0
        j = len(self.ls) - 1
        while i <= j:
            m = (i + j) // 2
            mv = ls[m][0]
            if l < mv:
                j = m - 1
            elif mv < l:
                i = m + 1
            else:
                return m
        
        # Remember this
        return j

    def addRange(self, left: int, right: int) -> None:
        ls = self.ls
        i = self.getindx(left)
        if len(ls) == 0:
            ls.append((left, right))
            return

        if i != -1 and left <= ls[i][1]:
            # In case
            start = ls[i][0]
        else:
            # Out case
            i += 1
            if i < len(ls) and right < ls[i][0]:
                ls.insert(i, (left, right))
                return
            else:
                start = left
        
        lastpopped = None
        while i < len(ls) and ls[i][0] <= right:
            lastpopped = ls.pop(i)
        
        if lastpopped is not None:
            ls.insert(i, (start, max(lastpopped[1], right)))
        else:
            ls.insert(i, (start, right))

    def removeRange(self, left: int, right: int) -> None:
        ls = self.ls
        i = self.getindx(left)
        if i != -1 and left < ls[i][1]:
            popped = ls.pop(i)
            if popped[0] < left:
                ls.insert(i, (popped[0], left))
                i += 1
            if right < popped[1]:
                ls.insert(i, (right, popped[1]))
                i += 1
        else:
            i += 1
        
        lastpopped = None
        while i < len(ls) and ls[i][0] < right:
            lastpopped = ls.pop(i)
        
        if lastpopped is not None and lastpopped[1] > right:
            ls.insert(i, (right, lastpopped[1]))
        

    def queryRange(self, left: int, right: int) -> bool:
        ls = self.ls
        i = self.getindx(left)
        if i == -1:
            return False
        if ls[i][1] < right:
            return False
        return True

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
