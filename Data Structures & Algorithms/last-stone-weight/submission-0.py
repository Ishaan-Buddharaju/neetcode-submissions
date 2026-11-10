from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones: 
            heappush(heap, -1 * stone)
        
        while len(heap) > 1: 
            x = heappop(heap)
            y = heappop(heap)
            if x != y: 
                newRock = abs(x - y) * -1
                heappush(heap, newRock)
            
        if len(heap) == 1:
            return -1 * heap[0]

        return 0 
