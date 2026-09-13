class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # brute force (O(n) time and space)
        # freq = {}
        # for num in nums:
        #     if num in freq:
        #         freq[num] = 2
        #     else: 
        #         freq[num] = 1
        
        # for k,v in freq.items():
        #     if v == 1: 
        #         return k
        
        # return -1

        # Take the bitwise op which finds the extra 1s
        # Since all appear twice, XOR leaves only the extra 1s
        res = 0
        for num in nums: 
            res ^= num

        return res


    