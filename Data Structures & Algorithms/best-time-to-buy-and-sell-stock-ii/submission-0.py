class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 1: 
            return 0
        
        prev = prices[0]
        i = 1
        while i < len(prices):
            curr = prices[i]
            if curr > prev:
                profit += curr - prev
            
            prev = curr
            i += 1
        
        return profit



        