class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {i: [] for i in range(len(nums) + 1)} # buckets of posisble counts
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq: 
                freq[nums[i]] += 1
            else: 
                freq[nums[i]] = 1
        for key,v in freq.items(): 
            buckets[v].append(key)
        result = []
        for i in range(len(nums), -1, -1):
            if k == 0: 
                return result
            if len(buckets[i]) != 0: 
                for num in buckets[i]:
                    print(str(num) + " " + str(i) + " " + str(k))
                    result.append(num)
                    k -= 1


            
            
        


