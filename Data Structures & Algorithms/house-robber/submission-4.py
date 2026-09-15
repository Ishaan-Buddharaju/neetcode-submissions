class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def helper(nums, i, cache):
            if i == 2:
                return nums[0]
            elif i < 2:
                return 0

            temp1 = None
            if i - 3 in cache: 
                temp1 = cache[i - 3]
            else:
                temp1 = helper(nums, i - 3, cache)
                cache[i - 3] = temp1
            
            temp2 = None
            if i - 2 in cache: 
                temp2 = cache[i - 2]
            else: 
                temp2 = helper(nums, i - 2, cache)
                cache[i - 2] = temp2

            return max(temp1 + nums[i - 3], temp2 + nums[i - 2])
        
        return helper(nums, len(nums) + 1, cache)
            





        