from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashset of nums and indicies
        # check if target - num[i] is in the hashset and not equal to i
        lookup = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in lookup and lookup[val] != i:
                return [i, lookup[val]]
        return 0
            
       
        

            



            
            
            
        