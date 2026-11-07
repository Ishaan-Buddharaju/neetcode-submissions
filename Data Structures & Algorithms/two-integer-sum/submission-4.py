from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashset of seen
        # check if target - num[i] is in the hashset and not equal to i
        seen=dict()
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in seen: 
                return [seen[remainder], i]
            else: 
                seen[nums[i]] = i
        

            
       
        

            



            
            
            
        