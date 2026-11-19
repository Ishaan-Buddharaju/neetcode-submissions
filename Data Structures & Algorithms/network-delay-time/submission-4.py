from heapq import heappush, heappop
from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = {}
        for u,v,t in times:
            if u in graph: 
                graph[u].append([v,t])
            else: 
                graph[u] = [[v,t]]

        heap = [[0, k]]
        time = 0
        visited = set()
        while heap: 
            curr = heappop(heap)
            while curr[1] in visited:
                if not heap:
                    break
                curr = heappop(heap)
            if curr[1] in visited:
                break
            visited.add(curr[1])
            time = curr[0]
            for edge in graph.get(curr[1], []):
                if edge[0] not in visited:
                    heappush(heap, [time + edge[1], edge[0]])
     
        if len(visited) < n:
            return -1

        return time
