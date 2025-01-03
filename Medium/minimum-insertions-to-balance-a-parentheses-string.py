class Solution:
    def minInsertions(self, s: str) -> int:
        i = 0
        insertions = 0
        nl = 0; nr = 0
        while True:
            while i < len(s) and s[i] == '(': nl += 1; i += 1
            while i < len(s) and s[i] == ')': nr += 1; i += 1
            if nr % 2 != 0: insertions += 1; nr += 1
            closes = int(nr / 2)
            if closes > nl:
                # More )) than (
                insertions += closes - nl
                nl = 0; 
                nr = 0
            else:
                # More ( than ))
                nl -= closes
                nr = 0
                
            if not i < len(s): break

        insertions += nl * 2
        return insertions
            



        

