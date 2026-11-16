from heapq import heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heappush(heap, (-1 * nums[i], i))

        output = [-1 * heap[0][0]]
        l = 1
        r = k
        while r < len(nums):
            heappush(heap, (-1 * nums[r], r))
            while heap[0][1] < l:
                heappop(heap)
            output.append(-1 * heap[0][0])
            l += 1
            r += 1
            
        return output