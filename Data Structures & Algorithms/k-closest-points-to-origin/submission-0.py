from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            pt = points[i] 
            dist = ((pt[0] - 0) ** 2 + (pt[1] - 0) ** 2) ** 0.5
            heappush(distances, (dist, i)) # since guarantee unique the index tie break won't change the answer
        res = []
        for i in range(k):
            idx = heappop(distances)[1]
            res.append(points[idx])
        return res