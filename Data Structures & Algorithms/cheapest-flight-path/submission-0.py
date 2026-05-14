class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # max of k stops
    # ret: cheapest price with at most k or -1 if not possible

        dist = {i: [float('inf'), float('inf')] for i in range(n)} # verticies: (cost, kth step)
        dist[src][0] = 0
        dist[src][1] = 0
        for i in range(n):
            for edge in flights:
                stepsFrom = dist[edge[0]][1]
                stepsTo = stepsFrom + 1
                currCost = edge[2] + dist[edge[0]][0]
                if currCost < dist[edge[1]][0] and stepsTo <= k + 1:
                    dist[edge[1]][0] = currCost
                    dist[edge[1]][1] = stepsTo
        
        if dist[dst][0] == float('inf'): 
            return -1
        
        return dist[dst][0]

        '''
        k = 2
        0 1      2
        0  0 
        1     200   
        2           
        3           
        '''


        