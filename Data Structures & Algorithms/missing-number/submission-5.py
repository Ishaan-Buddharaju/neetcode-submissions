class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # SORTING
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

        # HASHSET
        # expected = set([i for i in range(len(nums) + 1)])
        # for i in range(len(nums)):
        #     expected.remove(nums[i])

        # return expected.pop() # maintains the invariant that len(expected) == 1 now
        
        # MATH
        # expected = 0
        # prefix = 0
        # for i in range(len(nums)):
        #     expected += i + 1
        #     prefix += nums[i]
        # return expected - prefix