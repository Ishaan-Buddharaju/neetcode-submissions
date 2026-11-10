class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        n = n-1 + n-2 where base case of n < 1 = 1
        '''
        if n < 2: 
            return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        i = 2
        while i < n: 
            dp[i] = dp[i - 1] + dp[i - 2]
            i += 1
        return dp[n - 1]
        



        
     
