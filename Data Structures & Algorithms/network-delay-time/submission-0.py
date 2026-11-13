from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # run dijksta while visited is less than n
        # early exit if heap is empty and return -1
        # at the end return the final relaxation cost or the max of the time map
        heap = []
        visited = set()
        visited.add(k)
        costs = {i: float('inf') for i in range(1, n + 1)}
        costs[k] = 0
        curr = k
        cost = 0
        
        while (len(visited) != n):
            for ui, vi, ti in times:
                if ui != curr or vi in visited:
                    continue
                temp = cost + ti
                if temp < costs[vi]: # edge relaxtion
                    costs[vi] = temp
                heappush(heap, (temp, vi))
            while (curr in visited and len(heap) != 0):
                cost, curr = heappop(heap)
            if curr in visited: 
                return -1
            visited.add(curr)

        return cost       

        # while visited does not have all verticies
            # for each edge from curr
                # relax the cost to visit if not in visited
                # push (vert_to, costs[curr] + edge weight)
            # while (curr in visited and heap not empty):
                #curr is heappop
            # if curr in visited return -1
            # add curr to visited

        # return cost because it's the last cost we relaxed 
        
        