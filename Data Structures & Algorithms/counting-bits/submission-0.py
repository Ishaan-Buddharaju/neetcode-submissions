class Solution:
    def countBits(self, n: int) -> List[int]:
        prevPower2 = 0
        memo = [0] * (n + 1)
        for i in range(1, n + 1):
            if (i & (i - 1) == 0):
                prevPower2 = i
                memo[i] = 1
            else: 
                memo[i] = memo[prevPower2] + memo[i - prevPower2]
        
        return memo