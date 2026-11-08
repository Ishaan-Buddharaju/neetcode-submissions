class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        min speed is 1 / hr
        we want the min valid speed
        max speed is the max value for a given pile

        binary search with space being k
        - left starts at 1
        - right starts at max(piles) O(N)
        '''

        def canFinish(k, h):
            hoursNeeded = 0 
            for pile in piles: 
                hoursNeeded += (pile + k - 1) // k
                if hoursNeeded > h: 
                    return False
            return True

        l = 1
        r = max(piles)
        minRate = -1
        while l <= r: 
            m = l + (r - l) // 2
            print(m)
            if canFinish(m, h): 
                minRate = m
                r = m - 1
            else: 
                l = m + 1
            print("l" + str(l))
            print("r" + str(r))

        return minRate

    
            


        
                    
                




        


        




        

        
        