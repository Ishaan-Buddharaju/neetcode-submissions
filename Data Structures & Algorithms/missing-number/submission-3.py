class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = set([i for i in range(len(nums) + 1)])
        for i in range(len(nums)):
            expected.remove(nums[i])
        if (len(expected) != 1):
            print("cooked " + str(len(expected)))
        return expected.pop() # maintains the invariant that len(expected) == 1 now