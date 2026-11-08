class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # For each update of pointer prev != curr
        #       Prevents duplicates
        nums.sort()
        output = []
        prev1 = float('inf')
        for i in range(len(nums) - 2): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R: 
                val = nums[i] + nums[L] + nums[R]
                if val == 0:
                    output.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L - 1] and L < R: 
                        L += 1
                elif val > 0:
                    R -= 1
                else: 
                    L += 1
            prev1 = nums[i]  

        return output

        




        