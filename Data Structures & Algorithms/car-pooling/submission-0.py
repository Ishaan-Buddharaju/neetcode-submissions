from heapq import heapify, heappush, heappop
# Left to right scan with an events list
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Events list: (dist, e, cost) 
        # e: 0 or 1: 0 is from 1 is to
        # Cost is the number of passengers added or lost
        E = []

        for trip in trips:
            E.append((trip[1], trip[0], 0))
            E.append((trip[2], trip[0], 1))

        heapify(E)
        cur = 0

        while E:
            d, cost, event = heappop(E)

            if event == 0:
                cur += cost
            else:
                cur -= cost

            #print(cur)
            
            if cur > capacity and E[0][0] != d:

                return False

        return True
