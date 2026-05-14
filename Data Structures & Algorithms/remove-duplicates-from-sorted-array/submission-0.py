class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        prev_unique: int = None
        for val in nums:
            if val == prev: 
                List.pop(index)
            else: 
                prev_unique = val
            index += 1
        return len(nums)