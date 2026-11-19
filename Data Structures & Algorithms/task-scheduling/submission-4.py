class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Greedy
        # Can gap on the frequency then try to populate
        freq = [0] * 26
        for char in tasks: 
            freq[ord(char) - ord("A")] += 1
        
        freq.sort()
        maxf = freq[25]
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            count = freq[i]
            if count == 0:
                continue
            idle -= min(count, maxf - 1) 

        # A _ _ A _ _ A
        # BBB C
    
            
        if idle > 0:
            return len(tasks) + idle
        
        return len(tasks)
        


