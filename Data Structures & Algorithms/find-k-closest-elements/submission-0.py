class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        bestIdx = -1
        minCost = float('inf')
        cost = 0
        for i in range(len(arr) - k + 1):
            for j in range(i, i + k): 
                cost += abs(arr[j] - x)
            if cost < minCost: 
                bestIdx = i
                minCost = cost
            cost = 0
            
        return arr[bestIdx:bestIdx + k]

