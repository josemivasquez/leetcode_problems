class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        @cache
        def check(s1, s2, lcont, rcont):
            # 3 cases
            # some number
            # 2 letters and some counter
            # 2 letters and no counters
            # if len(s1) == 0 and len(s2) == 0:
            #     return lcont == rcont

            m = min(lcont, rcont)
            lcont -= m
            rcont -= m
            # if len(s1) == 0: 
            #     if lcont == 0:
            #         return rcont + len(s2) == 0
            #     if s2[0].isdigit():
            #         return somenumber(s2, s1, rcont, lcont)
            #     else:
            #         return twoletters_somecounter(s1, s2, lcont)
            # if len(s2) == 0:
            #     if rcont == 0:
            #         return lcont + len(s1) == 0
            #     if s1[0].isdigit():
            #         return somenumber(s1, s2, lcont, rcont)
            #     else:
            #         return twoletters_somecounter(s2, s1, rcont)

            if len(s1) > 0 and s1[0].isdigit():
                return somenumber(s1, s2, lcont, rcont)
            elif len(s2) > 0 and s2[0].isdigit():
                return somenumber(s2, s1, rcont, lcont)
            
            if lcont > 0:
                return twoletters_somecounter(s1, s2, lcont)
            elif rcont > 0:
                return twoletters_somecounter(s2, s1, rcont)
            
            return twoletters_nocounters(s1, s2)

        def somenumber(numstr, otherstr, numstrcont, otherstrcont):
            i = 0
            while i < len(numstr) and numstr[i].isdigit():
                c = check(numstr[i+1:], otherstr, numstrcont + int(numstr[:i+1]), 
                    otherstrcont)
                if c: return True
                i += 1
            return False
        
        def twoletters_somecounter(contstr, otherstr, cont):
            i = 0
            while i < len(otherstr) and not otherstr[i].isdigit() and cont > 0:
                i += 1
                cont -= 1
            
            otherstr = otherstr[i:]
            if len(otherstr) == 0:
                return len(contstr) + cont == 0
            
            elif otherstr[0].isdigit():
                return somenumber(otherstr, contstr, 0, cont)
            
            # Cont == 0
            return twoletters_nocounters(contstr, otherstr)

            
        def twoletters_nocounters(s1, s2):
            i = 0
            j = 0
            while i < len(s1) and j < len(s2) and not s1[i].isdigit() and not s2[j]
                .isdigit() and s1[i] == s2[j]:
                i += 1
                j += 1

            s1 = s1[i:]
            s2 = s2[j:]
            
            if len(s1) == 0:
                return len(s2) == 0
            elif len(s2) == 0:
                return False
            elif s1[0].isdigit():
                return somenumber(s1, s2, 0, 0)
            elif s2[0].isdigit():
                return somenumber(s2, s1, 0, 0)
            else:
                return False

        
        return check(s1, s2, 0, 0)


