class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        prefix = [0] * len(height)
        prefix[0] = height[0]
        maxL = height[0]
        maxR = height[-1]
        suffix = [0] * len(height)
        suffix[-1] = height[-1]

        for i in range(1, len(height)):
            if height[i] > maxL:
                maxL = height[i]
            prefix[i] = maxL
            suffixIdx = len(height) - i - 1
            if height[suffixIdx] > maxR:
                maxR = height[suffixIdx]
            suffix[suffixIdx] = maxR
        
        for i in range(len(height)):
            total += max(min(prefix[i], suffix[i]) - height[i], 0)
        
        return total
