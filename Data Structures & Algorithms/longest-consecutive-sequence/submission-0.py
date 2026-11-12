from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        First idea is to sort and use two pointers to count the length
        O(nlog n) time then O(log n) or O(1) space

        Next idea is to use hash map to store left and right flags for each
        Then iterate on that left and right until I find the edge. 
        '''

        lookup = defaultdict(int)
        maxSequence = 0

        for num in nums: 
            lookup[num] = 1

        currSequence = -1
        for num in list(lookup):
            lookup[num] = 0
            currKey = num
            delta = 1
            while (delta):
                currSequence += 1
                currKey -= 1
                delta = lookup[currKey]
                lookup[currKey] = 0
            delta = 1
            currKey = num
            while (delta):
                currSequence += 1
                currKey += 1
                delta = lookup[currKey]
                lookup[currKey] = 0
            if maxSequence < currSequence:
                maxSequence = currSequence
            currSequence = -1
        
        return maxSequence


            




        