class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while (l < r):
            m = l + (r  - l) // 2
            if nums[m] > nums[r]: # right half is unsorted
                l = m + 1
            else: # left half is unsorted or sorted minimum
                r = m
                

        return nums[r]