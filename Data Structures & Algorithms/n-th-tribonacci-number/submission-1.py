class Solution:
    def tribonacci(self, n: int) -> int:
        a, b , c = 0, 1, 1
        if n == 0:
            return a
        elif n < 3: 
            return b

        i = 3
        while i <= n: 
            temp = c
            c = a + b + c
            a = b
            b = temp
            i += 1
            
        return c
        