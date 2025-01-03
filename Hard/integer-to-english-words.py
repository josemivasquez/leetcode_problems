class Solution:
    def numberToWords(self, num: int) -> str:
        wrds = {
            '0' : 'Zero' , '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 
                'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
        }
        cases1x = {
            '10' : 'Ten', '11' : 'Eleven', '12' : 'Twelve', '13' : 'Thirteen', '14' : 
                'Fourteen', '15' : 'Fifteen', '16' : 'Sixteen',
            '17' : 'Seventeen', '18' : 'Eighteen', '19' : 'Nineteen'
        }
        pref2 = {'2' : 'Twenty', '3': 'Thirty', '4' : 'Forty', '5' : 'Fifty', '6' : 
            'Sixty', '7' : 'Seventy', '8' : 'Eighty', '9' : 'Ninety'}
        dimensions = ['Thousand', 'Million', 'Billion', 'Trillion']


        def rf(n):
            if len(n) == 3:
                if n[0] == '0':
                    return rf(n[1:])
                if n[1:] == '00':
                    return wrds[n[0]] + ' Hundred'
                return wrds[n[0]] + ' Hundred ' + rf(n[1:])
            if len(n) == 2:
                if n[0] == '1':
                    return cases1x[n]
                if n[0] == '0':
                    return rf(n[1:])
                if n[1] == '0':
                    return pref2[n[0]]
                return pref2[n[0]] + ' ' + rf(n[1:])
            if len(n) == 1:
                return wrds[n]
        
        num = str(num)
        i = len(num) - 1
        ansi = i
        i -= 3
        res = ''
        if num[max(0, i+1):ansi+1] != '000':
            res += rf(num[max(0, i+1):ansi+1])
        
        cnt = 0
        while i >= 0:
            ansi = i
            i -= 3
            if num[max(0, i+1):ansi+1] == '000':
                cnt += 1
                continue
            ansres = res
            res = rf(num[max(0, i+1):ansi+1]) + ' ' + dimensions[cnt]
            if ansres != '':
                res += ' ' + ansres
            cnt += 1
        
        if res[-1] == ' ':
            res = res[:-1]
        
        return res







                


