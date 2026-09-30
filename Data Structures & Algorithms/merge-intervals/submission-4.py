class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def hasOverlap(low, high):
            if low[1] >= high[0]:
                return True

            return False


        intervals.sort(key= lambda x: (x[0], x[1]))
        result = [intervals[0]]
        i = 0
        for interval in intervals: 
            if hasOverlap(result[i], interval): 
                result[i][1] = max(result[i][1], interval[1])
            else:
                result.append(interval) 
                i += 1
        return result


