class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        r = ''
        i = 0
        cnt = 'a'
        while i < len(sentence):
            w = ''
            while i < len(sentence) and sentence[i] != ' ': 
                w += sentence[i]
                i += 1
            if w[0] in vowels:
                w += 'ma'
            else:
                w = w[1:] + w[0] + 'ma'
            r += w + cnt
            cnt += 'a'
            r += ' '
            i += 1
        

        r = r[:-1]
        return r
            

