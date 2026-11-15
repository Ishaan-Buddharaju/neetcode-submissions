class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # expected = set([i for i in range(len(nums) + 1)])
        # for i in range(len(nums)):
        #     expected.remove(nums[i])

        # return expected.pop() # maintains the invariant that len(expected) == 1 now
        expected = 0
        prefix = 0
        for i in range(len(nums)):
            expected += i + 1
            prefix += nums[i]
        return expected - prefix