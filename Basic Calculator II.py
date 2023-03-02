from math import trunc
class Solution:
    def calculate(self, s: str) -> int:
        summ = []
        op = []
        num = ""
        for c in s:
            if c == " ":
                continue
            if c.isdigit():
                num += c
            elif op:
                operater = op.pop()
                if operater == "+":
                    summ.append(int(num))
                if operater == "-":
                    summ.append(int(num)*-1)
                if operater == "*":
                    summ[-1] *= int(num)
                if operater == "/":
                    summ[-1] = trunc(summ[-1] / int(num))
                num = ""
                op.append(c)
            else:
                summ.append(int(num))
                num = ""
                op.append(c)
        if op:
            operater = op.pop()
            if operater == "+":
                summ.append(int(num))
            if operater == "-":
                summ.append(int(num)*-1)
            if operater == "*":
                summ[-1] *= int(num)
            if operater == "/":
                summ[-1] = trunc(summ[-1] / int(num))
        else:
            summ.append(int(num))

        return sum(summ)
    
s = Solution()
print(s.calculate("14-3/2"))