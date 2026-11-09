class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort on start then end times
        # This gives [[1, 3], [1,5], [2, 5]]
        # Then merge until can't. Update to next and continue
        if len(intervals) < 2: 
            return intervals
        intervals.sort(key=lambda x: [x[0], x[1]]) # nlogn amortized
        output = []
        p = 1
        curr = intervals[0]
        while p < len(intervals):
            i1 = curr
            i2 = intervals[p]
            a, b, c , d = i1[0], i1[1], i2[0], i2[1]
            if (max(a, c) <= min(b, d)): # overlap
                curr = [min(a, c), max(b, d)]
            else: 
                output.append(curr)
                curr = i2
            p += 1
        output.append(curr)
        return output

