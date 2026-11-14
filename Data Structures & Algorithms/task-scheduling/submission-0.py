from heapq import heappush, heappop, heapify
from collections import deque, defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1

        curr = None
        q = deque()
        cycles = 0
        heap = []
        for k,v in freq.items():
            heappush(heap, [-v, k])
        del freq

        while len(heap) > 0 or len(q) > 0:
            if q and cycles - q[0][1] > n: # [[v,k], cycle]
                curr, cycle = q.popleft()
                heappush(heap, curr)
            
            if heap: 
                curr = heappop(heap)
                curr[0] += 1
                if curr[0] != 0: 
                    q.append([curr, cycles])

            cycles += 1
            
        return cycles
        
        

