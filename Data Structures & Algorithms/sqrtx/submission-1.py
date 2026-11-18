class Solution:
    def mySqrt(self, x: int) -> int:
        # searching for the perfect square between 1 and x
        l = 0

        r = x // 2 if x > 1 else 1
        
        while (l <= r):
            m = l + (r - l) // 2
            if m * m == x:
                return m
            elif m * m > x:
                r = m - 1
            else:
                l = m + 1
        
        return r