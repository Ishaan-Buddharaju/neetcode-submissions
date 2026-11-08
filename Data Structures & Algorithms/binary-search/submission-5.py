class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 # 4
        r = len(nums) - 1

        while (l <= r):
            m = l + (r - l) // 2
            print(m)
            val = nums[m]
            if val == target: 
                return m
            elif val < target: 
                l = m + 1 
            else: 
                r = m - 1

        return -1
