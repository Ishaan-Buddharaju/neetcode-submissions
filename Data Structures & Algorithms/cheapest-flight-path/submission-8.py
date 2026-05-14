class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # max of k stops
    # ret: cheapest price with at most k or -1 if not possible

        dist = [float('inf')] * n# verticies: (cost, kth step)
        dist[src] = 0
        # dist[src][1] = 0
        for i in range(k + 1):
            tmp = dist.copy() # copy
            for i, j, w in flights:
                # stepsFrom = prev[edge[0]][1]
                # stepsTo = stepsFrom + 1 
                currCost = w + dist[i] 
                if (currCost < tmp[j]):
                    tmp[j] = currCost
                    # dist[edge[1]][1] = stepsTo
            dist = tmp
            
        
        if dist[dst] == float('inf'): 
            return -1
        
        return dist[dst]


        