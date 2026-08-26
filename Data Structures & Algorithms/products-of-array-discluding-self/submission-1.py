class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first solution, brute force
        prefix = []
        curr = 1
        for i in range(len(nums)):
            curr *= nums[i]
            prefix.append(curr)
        suffix = [1] * len(nums)
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            curr *= nums[i]
            suffix[i] = curr
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(suffix[i + 1])
            elif i == len(nums) - 1:
                output.append(prefix[i - 1])
            else:
                output.append(prefix[i - 1] * suffix[i + 1])
        return output
        
        
                
        