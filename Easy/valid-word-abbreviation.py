class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if not abbr[j].isdigit():
                if abbr[j] != word[i]:
                    return False
                j += 1
                i += 1
                continue
            n = int(abbr[j])
            if n == 0:
                return False
            j += 1
            while j < len(abbr) and abbr[j].isdigit():
                n = n * 10 + int(abbr[j])
                j += 1
            i += n
        
        if i != len(word) or j != len(abbr):
            return False
        return True
