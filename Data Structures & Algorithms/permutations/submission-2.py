class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        options = [True] * len(nums)
        self.backtrack(nums, options, [])
        return self.result

    def backtrack(self, nums, options, curr):
        if len(nums) == len(curr):
            self.result.append(curr)
            return 

        for i in range(len(options)): 
            if options[i]: 
                options[i] = False
                self.backtrack(nums, options, curr + [nums[i]])
                options[i] = True
        
        return