class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lookup = {0: 1}
        total = 0
        count = 0
        for i in range(len(nums)):
            total += nums[i]
            target = total - k
            if target in lookup:
                count += lookup[target]
            if total in lookup: 
                lookup[total] += 1
            else:
                lookup[total] = 1
        
        return count
