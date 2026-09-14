class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # MEMOIZATION
        # '''
        # # Find the global min cost to reach index len(cost)

        # step 4
        # 1 1
        # 1 1.  2 1
        # '''

        # cache = {} # key is step, value is the optimal local cost
        # def helper(cost, cache, i):
        #     if i <= 1:
        #         return 0

        #     if i in cache:
        #         return cost[i]
            
        #     temp1 = -1
        #     if i - 1 in cache: 
        #         temp1 = cache[i - 1]
        #     else:
        #         temp1 = helper(cost, cache, i - 1) + cost[i - 1]
        #         cache[i - 1] = temp1

        #     temp2 = -1
        #     if i - 2 in cache:
        #         temp2 = cache[i - 2]
        #     else:
        #         temp2 = helper(cost, cache, i - 2) + cost[i - 2]
        #         cache[i - 2] = temp2

        #     return min(temp1, temp2)
        # return helper(cost, cache, len(cost))
        '''
        BOTTOM UP DP
        '''
        n = len(cost)
        dp = [0] * (n + 1)
        
        i = 2
        while i <= n:
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
            i += 1
        
        return dp[n]

        

            

            




