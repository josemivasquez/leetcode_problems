class Solution:
    def calculate(self, s: str) -> int:
        # Just putting this here, the beats % 5 -> 65
        digits_set = {str(i) for i in range(0, 10)}
        def isdigit(c):
            return c in digits_set
        nums = []
        ops = []
        current_num = 0
        for c in s:
            if c == ' ': continue
            if isdigit(c): current_num = current_num * 10 + int(c)
            if c in {'+', '-', '*', '/'}:
                ops.append(c)
                nums.append(current_num)
                current_num = 0
        nums.append(current_num)

        current_num = 0
        current_mul = nums[0]

        for n, op in zip(nums[1:], ops):
            if op == '*': current_mul *= n
            elif op == '/': current_mul = int(current_mul / n)
            elif op == '+':
                current_num += current_mul
                current_mul = n
            else:
                current_num += current_mul
                current_mul = -n
            
        current_num += current_mul
        return current_num
                

