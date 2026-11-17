class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = [0] * (n + 1)
        for i in range(0, n + 1):
            memo[i] = memo[i >> 1] + (i & 1)
        
        return memo