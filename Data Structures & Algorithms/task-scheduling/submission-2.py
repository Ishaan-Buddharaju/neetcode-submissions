from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Ordering the tasks
        # Each "event" is a cpu cycle
        # Minimizing wait time means interleving the most with the next most frequent at every cycle

        freq = {}
        for task in tasks:
            if task in freq:
                freq[task] -= 1
            else:
                freq[task] = -1

        # MIN HEAP of negatives to make it max   
        heap = []
        for task, count in freq.items():
            heapq.heappush(heap, [count, task])
        
        cycle = 0
        q = deque()
        while heap or q:
            cycle += 1

            if heap:
                curr = heapq.heappop(heap)
                curr[0] += 1
                if curr[0] < 0:
                    q.append([curr, cycle + n])
                    
            if q and q[0][1] == cycle:
                ready = q.popleft()[0]
                heapq.heappush(heap, ready)

        return cycle

