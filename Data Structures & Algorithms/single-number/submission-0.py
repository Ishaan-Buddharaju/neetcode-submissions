class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # brute force (O(n) time and space)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] = 2
            else: 
                freq[num] = 1
        
        for k,v in freq.items():
            print(str(k) + " " + str(v))
            if v == 1: 
                return k
        
        return -1
    