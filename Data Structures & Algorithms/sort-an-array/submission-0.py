class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    def mergeSort(self, nums) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        l, r = 0, 0
        res = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else: 
                res.append(right[r])
                r += 1
        
        res.extend(left[l:])
        res.extend(right[r:])

        return res

    