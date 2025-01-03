class MagicDictionary:

    def __init__(self):
        self.tries = dict()

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            l = len(w)
            if l not in self.tries:
                self.tries[l] = dict()
            root = self.tries[l]
            cn = root
            for c in w:
                if c not in cn:
                    cn[c] = dict()
                cn = cn[c]
    
        
    def search(self, searchWord: str) -> bool:
        def branch_search(root, w):
            cn = root
            for c in w:
                if c not in cn:
                    return False
                cn = cn[c]
            return True

        if len(searchWord) not in self.tries:
            return False

        root = self.tries[len(searchWord)]
        cn = root
        indx = 0
        for c in searchWord:
            for r in cn:
                if r == c: continue
                if branch_search(cn[r], searchWord[indx+1:]):
                    return True
            if c not in cn:
                return False
            cn = cn[c]
            indx += 1
        
        return False

        

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
