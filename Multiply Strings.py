class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        add_table = {}
        for i in range(10):
            for j in range(10):
                add_table[(str(i),str(j))] = str(i+j)
        
        mult_table = {}
        for i in range(10):
            for j in range(10):
                mult_table[(str(i),str(j))] = str(i*j)
        
        def add(x, y):
            length = max(len(x), len(y))
            x = "0" * (length-len(x)) + x
            y = "0" * (length-len(y)) + y

            ans = ""
            carry = ""
            for i in range(length-1,-1,-1):
                summ = add_table[(x[i],y[i])]
                if carry:
                    summ = add(summ, carry)
                ans = summ[-1] + ans
                carry = summ[:-1]
            return carry + ans

        def mult_digit(num1, digit):
            ans = ""
            carry = ""

            for i in num1[::-1]:
                prod = mult_table[i,digit]
                if carry:
                    prod = add(prod, carry)
                ans = prod[-1] + ans
                carry = prod[:-1]
            return carry + ans

        ans = "0"
        tens = 0
        for i in num2[::-1]:
            prod = mult_digit(num1,i) + "0" * tens
            ans = add(prod, ans)
            tens += 1
        
        ans = ans.lstrip("0")
        if not ans:
            return "0"
        return ans

s = Solution()
print(s.multiply("123","456"))