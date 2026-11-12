class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack vs monotonic stack
        # maintain that each next is leq prev. Then unwind
        n = len(temperatures)
        stack = []
        result = [0] * n
        for i in range(n):
            curr = temperatures[i]
            while ((not len(stack) == 0) and (curr > stack[-1][0])): 
                update = stack.pop()
                idx = update[1]
                days = i - idx
                result[idx] = days
            stack.append((curr, i))
        return result
            