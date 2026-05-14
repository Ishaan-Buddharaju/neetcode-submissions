class Solution:
    def rob(self, nums: List[int]) -> int:
        # vertices
        # iterate over list
        # if not i + 2 > len(nums) - 1
        # i + 2 is alternate
        # i + 3 is skip 
        # 
        # dist hashmap of len nums
        # all distances are ininity other than first house
        # for each v in vertices
        #   if cost from prev to next is less that before 
        #   relax edge
        # money = max(nums[0] + money(nums[2:], nums[1] + money(nums[3:])))
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        left = nums[0] + self.rob(nums[2:])
        right = nums[1] + self.rob(nums[3:])

        return max(left, right) 

        