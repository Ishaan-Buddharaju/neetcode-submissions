class Solution:
    memo = {1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:
        # 5
        # 1         2
        # 1   2     1   2
        # 1  2
        # 1 2 1
        # 1
        # paths(n) = paths(n - 1) + paths(n - 2)
        # paths (1) = 1 paths(2) = 2
        self.memo = {1: 1, 2: 2}
        return self.helper(n)


    def helper(self, n): 
        if n in self.memo: 
            return self.memo[n]
        
        res = self.helper(n - 1) + self.helper(n - 2)
        self.memo[n] = res
        return res



        
     
