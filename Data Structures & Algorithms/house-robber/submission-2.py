class Solution:
    memo = {}
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
        memo = {}
        return self.helper(0, nums)


    def helper(self, i, nums):
        if i >= len(nums):
            return 0
        if i in self.memo:
            return self.memo[i]

        result = max(nums[i] + self.helper(i + 2, nums), self.helper(i + 1, nums))
        self.memo[i] = result
        return result




        