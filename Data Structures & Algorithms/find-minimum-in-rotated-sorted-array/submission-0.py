class Solution:
    def findMin(self, nums: List[int]) -> int:
        # What if I search the rotation space instead of the list
        # 0 to len(nums) - 1
        # search for index where nums[i - 1] is greater than num[i]
        # if num[i] > nums[i - 1] go left 

        l = 0
        r = len(nums) - 1

        while (l <= r):
            m = l + (r - l) // 2

            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[l]:
                l = m + 1
            else: 
                return nums[r]
            
