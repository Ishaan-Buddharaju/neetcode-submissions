class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # each index is a pile where value is the height
        # h is hours to eat
        # return the min hourly rate I can eat
        
        R = max(piles)
        L = 1
        minimumRate = max(piles)
        while L <= R: 
            mid = (L + R) // 2
            if self.canFinishEating(piles, mid, h):
                minimumRate = mid
                R = mid - 1
            else: 
                L = mid + 1
        return minimumRate
            
        
    def canFinishEating(self, piles: List[int], k: int, h: int) -> bool: 
        duration = 0
        for pile in piles: 
            hours = (pile + k - 1) // k
            duration += hours
            if duration > h:
                print("False with k = " + str(k))
                return False
        print("True with k = " + str(k))
        return True
        


        




        

        
        