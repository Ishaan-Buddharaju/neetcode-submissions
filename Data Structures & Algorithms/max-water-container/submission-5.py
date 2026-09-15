class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = -1
        L = 0
        R = len(heights) - 1

        while L < R:
            height = min(heights[L], heights[R])
            currArea = height * (R - L)
            if currArea > maxArea:
                maxArea = currArea
            
            if heights[L] > heights[R]:
                R -= 1
            else: 
                L += 1

            

        return maxArea 

            




            