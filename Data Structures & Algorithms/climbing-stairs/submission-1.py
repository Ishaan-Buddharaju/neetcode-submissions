class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        There are ways to get to each step
        It's permutations of ways to get to each step

        Ex

        5
        4 3
        2 3   1 2
        1 0. 1 2   0.   1 0  

        Can use memoization to recall ways to get to each
        '''

        def helper(n: int, cache: dict[int: int]) -> int:
            if n in cache: 
                return cache[n]
            
            if n <= 1:
                return 1
            
            temp1 = helper(n - 1, cache)
            cache[n - 1] = temp1 
            temp2 = helper(n - 2, cache)
            cache[n - 2] = temp2

            cache[n] = temp1 + temp2
            return cache[n]

        cache = {}
        return helper(n, cache)


        



        
     
