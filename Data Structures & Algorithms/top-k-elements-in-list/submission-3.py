class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # Use counting sort on the requency array since the range is limited
        # freq = {i: 0 for i in range(-1000, 10001)}
        # for i in range(len(nums)): 
        #     freq[nums[i]] += 1
        # # Now we have freq {0: 2, 1: 0, 3: 15 ...}
        # # sort keys by freqency then return top k
        # return sorted(freq, key = freq.get, reverse = True)[:k]
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq: 
                freq[nums[i]] += 1
            else: 
                freq[nums[i]] = 1
        return sorted(freq, key = freq.get, reverse = True)[:k]

