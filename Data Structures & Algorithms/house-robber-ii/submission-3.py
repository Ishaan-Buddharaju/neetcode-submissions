class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Max rob at i is max of i - 2, i - 3

        Base case: 
            index of i + 1, i + 2

        memo the prev max
        '''
        n = len(nums)
        memo1 = {}
        memo2 = {}
        def helper(i, nums, memo):
            if i < 0: 
                return 0
            elif i == 0: 
                return nums[0]
        
            c1 = i - 1
            c2 = i - 2
            if c1 not in memo: 
                memo[c1] = helper(c1, nums, memo)
            if c2 not in memo: 
                memo[c2] = helper(c2, nums, memo)
            return max(memo[c1], nums[i] + memo[c2])
        if len(nums) == 1:
            return nums[0]

        return max(helper(n - 2, nums[1:], memo1), helper(n - 2, nums[:-1], memo2))
        

            
        
        
