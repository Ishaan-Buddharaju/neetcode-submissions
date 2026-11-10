class Solution:
    def rob(self, nums: List[int]) -> int:
        # max at 0th is nums[0th], max at 1st is nums[1]
        # max at 2nd is max(nums[2 - 2] + nums[2], nums[2 - 1])
        # track a, b, c where a is n - 2, b is n - 1, c is the max output of curr

        n = len(nums)
        
        if n < 3: 
            return max(nums)
        a = nums[0] # 2
        b = max(a, nums[1])
        i = 2 
        c = -1
        while i < n: 
            c = max(a + nums[i], b) # 3, 
            a = b # 1
            b = c # 3
            i += 1

        return c
            





        