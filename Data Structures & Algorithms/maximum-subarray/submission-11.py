class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for R in range(len(nums)):

            if (currSum < 0):
                L = R
                currSum = 0

            currSum += nums[R]
            if currSum > maxSum:
                maxSum = currSum


        return maxSum


        