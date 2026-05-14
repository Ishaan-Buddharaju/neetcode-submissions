class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # max of k stops
    # ret: cheapest price with at most k or -1 if not possible

        dist = {i: [float('inf'), float('inf')] for i in range(n)} # verticies: (cost, kth step)
        dist[src][0] = 0
        dist[src][1] = 0
        for i in range(k + 1):
            prev = dist.copy() # copy
            for edge in flights:
                stepsFrom = prev[edge[0]][1]
                stepsTo = stepsFrom + 1 
                currCost = edge[2] + prev[edge[0]][0] 
                if (currCost < prev[edge[1]][0]) and ((stepsTo == k + 1 and edge[1] == dst) or (stepsTo < k + 1)):
                    dist[edge[1]][0] = currCost
                    dist[edge[1]][1] = stepsTo
                    break
        
        if dist[dst][0] == float('inf'): 
            return -1
        
        return dist[dst][0]


        