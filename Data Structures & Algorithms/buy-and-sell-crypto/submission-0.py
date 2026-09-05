class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0
        for R in range(1, len(prices)):
            delta = prices[R] - prices[L]
            if delta < 0:
                L = R
            elif delta > profit:
                profit = delta
        
        return profit
            
            

            