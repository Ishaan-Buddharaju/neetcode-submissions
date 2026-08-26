class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # track a curr max and recalc each time
        maxArea = -1
        maxHeight = - 1
        # for i in range(len(heights) - 1):
        #     for j in range(i, len(heights)):
        #         currVolume = min(heights[i], heights[j]) * (j - i)
        #         if currVolume > maxVolume:
        #             maxVolume = currVolume 
        
        # return maxVolume

        L = 0
        R = len(heights) - 1
        while L < R: 
            currHeight = min(heights[L], heights[R])
            currArea = currHeight * (R - L)
            if currArea > maxArea:
                maxArea = currArea

            if heights[L] >= heights[R]:
                R -= 1
            else:
                L += 1
        
        return maxArea



            