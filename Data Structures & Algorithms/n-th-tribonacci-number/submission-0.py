class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3: 
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1

        i = 3
        while i <= n: 
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
            i += 1
            
        return dp[n]
        