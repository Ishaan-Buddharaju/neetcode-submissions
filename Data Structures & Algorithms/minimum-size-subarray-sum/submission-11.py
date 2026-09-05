class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        total = 0
        minLength = float('inf')
        for R in range(len(nums)):
            total += nums[R]
            while total >= target: 
                length = R - L + 1
                if length < minLength: 
                    minLength = length
                total -= nums[L]
                L += 1
                 
        
        return minLength if minLength != float('inf') else 0