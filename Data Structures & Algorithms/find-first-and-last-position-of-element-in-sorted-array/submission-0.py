class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        def binarySearch(l: int, r: int, searchStart: bool): 
            solution = -1
            while (l <= r):
                m = l + (r - l) // 2
                val = nums[m]
                if val == target: 
                    solution = m
                    if searchStart:      
                        r = m - 1
                    else: 
                        l = m + 1
                elif val < target: 
                    l = m + 1
                else: 
                    r = m - 1
            return solution

        return [binarySearch(l, r, True), binarySearch(l, r, False)]