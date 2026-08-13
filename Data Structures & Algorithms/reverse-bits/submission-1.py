class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        digits = 32
        while (n != 0): 
            if n % 2 == 1:
                binary = '1' + binary
            else: 
                binary = '0' + binary
            n //= 2
            digits -= 1
        binary = '0' * digits + binary
    
        result = 0
        count = 31
        for digit in binary: 
            if digit == '1': 
                result += 2 ** (31 - count)
            count -= 1
        return result