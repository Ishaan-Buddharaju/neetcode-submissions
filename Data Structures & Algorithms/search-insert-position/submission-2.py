class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Recursive
        # def binarySearch(l, r):
        #     print(str(l) + " and " + str(r))
        #     if l > r: 
        #         print("here")
        #         return l
        #     midpoint = l + (r - l) // 2
        #     val = nums[midpoint]
        #     if val == target: 
        #         return midpoint
        #     elif val < target: 
        #         return binarySearch(midpoint + 1, r)
        #     else: 
        #         return binarySearch(l, midpoint - 1)
            
        # return binarySearch(0, len(nums) - 1)

        # Iterative
        l, r = 0, len(nums) - 1
        while (l <= r): 
            m = l + (r - l) // 2
            val = nums[m]
            if val == target: 
                return m
            elif val > target: 
                r = m - 1
            else:
                l = m + 1
        
        return l