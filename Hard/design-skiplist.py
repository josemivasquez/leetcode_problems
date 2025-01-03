import random

def coinflip():
    return random.random() > 0.5

class Node():
    def __init__(self, data, reps=1):
        self.top = None
        self.below = None
        self.left = None
        self.right = None
        self.data = data
        self.reps = reps

class Skiplist:
    def __init__(self):
        self.head = Node(float('-inf'))

    def _search(self, target: int) -> bool:
        path = []
        ans = None
        cn = self.head
        while True:
            while cn is not None and cn.data <= target:
                ans = cn
                cn = cn.right
            path.append(ans)
            cn = ans
            if cn.below is None:
                break
            cn = cn.below
        
        return path
    
    def search(self, target):
        node = self._search(target)[-1]
        if node.data == target:
            return True
        else:
            return False

    def add(self, num: int) -> None:
        path = self._search(num)
        icn = len(path) - 1
        cn = path[icn]
        
        if cn.data == num:
            # Reps only in the last level
            cn.reps += 1
            return
        
        # Insert on the last level
        newnode = Node(num)
        if cn.right is not None:
            cn.right.left = newnode
            newnode.right = cn.right
        cn.right = newnode
        newnode.left = cn
        ansnewnode = newnode

        icn -= 1
        cn = path[icn]
        # Intermidiate levels
        while icn >= 0 and coinflip():
            # Go up
            newnode = Node(num)
            if cn.right is not None:
                cn.right.left = newnode
                newnode.right = cn.right
            cn.right = newnode
            newnode.left = cn
            newnode.below = ansnewnode
            ansnewnode.top = newnode
            ansnewnode = newnode

            icn -= 1
            cn = path[icn]
        
        if icn >= 0:
            return
        
        # New levels
        while coinflip():
            newnode = Node(num)
            anshead = self.head
            newhead = Node(float('-inf'))
            newhead.below = anshead
            anshead.top = newhead
            newhead.right = newnode
            newnode.left = newhead
            newnode.below = ansnewnode
            ansnewnode.top = newnode

            self.head = newhead
            ansnewnode = newnode

    def erase(self, num: int) -> bool:
        cn = self._search(num)[-1]
        if cn.data != num:
            return False
        if cn.reps > 1:
            cn.reps -= 1
            return True
        
        while cn is not None:
            if cn.left is not None:
                cn.left.right = cn.right
            if cn.right is not None:
                cn.right.left = cn.left
            cn = cn.top
        
        while self.head.right is None:
            self.head = self.head.below
        
        return True
    
    def tomt(self):
        ls = []
        cn = self.head
        anscn = None
        while cn is not None:
            ls.append([])
            anscn = cn
            cn = cn.below
        
        cn = anscn
        while cn is not None:
            ncn = cn
            i = len(ls) - 1
            while ncn is not None:
                ls[i].append( str((ncn.data, ncn.reps)) )
                ncn = ncn.top
                i -= 1
            while i >= 0:
                ls[i].append(' ')
                i -= 1
            cn = cn.right
        
        return ls
        
    def __str__(self):
        ls = self.tomt()
        res = ''
        for l in ls:
            for e in l:
                res += e
            res += '\n'
        
        return res
