class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low <= high:
            if target > nums[mid]:
                low = mid + 1
                mid = (high + low) // 2
            elif target < nums[mid]:
                high = mid - 1
                mid = (high + low) // 2
            else: 
                return mid
            
        return -1
