class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {num: idx for idx, num in enumerate(nums)}
        result = []
        for i in range(len(nums)):
            key = target - nums[i]
            if key in lookup.keys():
                return [i, lookup[key]]

        return []


            
            
            
        