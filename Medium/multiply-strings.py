class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
    
        # Initialize result as a list of zeros
        result = [0] * (len(num1) + len(num2))
        
        # Reverse both numbers to make the position handling easier
        num1, num2 = num1[::-1], num2[::-1]
        
        # Loop through each digit in num1
        for i in range(len(num1)):
            for j in range(len(num2)):
                # Multiply the current digits and add the result to the 
                    corresponding position in the result list
                result[i + j] += int(num1[i]) * int(num2[j])
                # Handle carry over
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # Reverse the result list to get the correct order and convert to string
        result = result[::-1]
        
        # Remove leading zeros and convert list to string
        while result[0] == 0 and len(result) > 1:
            result.pop(0)
        
        return ''.join(map(str, result))
        

        def str_sum(n1, n2):
            max_len = max(len(n1), len(n2))
            n1 = '0' * (max_len - len(n1)) + n1
            n2 = '0' * (max_len - len(n2)) + n2

            n1 = n1[::-1]
            n2 = n2[::-1]

            carrier = 0
            result = ''
            for d1, d2 in zip(n1, n2):
                s = str(int(d1) + int(d2) + carrier)
                if len(s) >= 2: carrier = 1
                else: carrier = 0
                result += s[-1]
            
            if carrier > 0:
                result += '1'
                carrier = 0

            return result[::-1]

        def str2int(s):
            response = 0
            order = 0
            for i in reversed(s):
                response += int(i) * (10 ** (order))
                order += 1
            return response
        
        return str(str2int(num1) * str2int(num2))
        # if num1 == "0" or num2 == "0": return "0"

        # if len(num1) > len(num2):
        #     minnum = num2; maxnum = num1
        # else:
        #     minnum = num1; maxnum = num2
        
        # minint = str2int(minnum)
        # response = ''
        # for i in range(minint):
        #     response = str_sum(response, maxnum)
        # return response

        if num1 == "0" or num2 == "0": return "0"
        result = ''
        carrier = 0
        digitorder = 0
        for d2 in reversed(num2):
            factor = ''
            for d1 in reversed(num1):
                m = str(int(d1) * int(d2) + carrier)
                if len(m) > 1: carrier = int(m[0])
                else: carrier = 0
                factor += m[-1]
            
            if carrier > 0:
                # Leading Carrier
                factor += str(carrier)
                carrier = 0
            
            factor = factor[::-1] + '0' * digitorder
            result = str_sum(result, factor)
            digitorder += 1
        
        # leading_zeros = 0
        # while True:
        #     if leading_zeros < len(result) and result[leading_zeros] == '0':
        #         leading_zeros += 1
        #     else:
        #         break
        # result = result[leading_zeros:]
        # if result == '':
        #     result = '0'

        return result

            
        
                
                





        
