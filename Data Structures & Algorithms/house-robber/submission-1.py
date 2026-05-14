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
        return helper(0, nums)

memo = {}
def helper(i, nums):
    if i >= len(nums):
        return 0
    if i in memo:
        return memo[i]

    result = max(nums[i] + helper(i + 2, nums), helper(i + 1, nums))
    memo[i] = result
    return result




        