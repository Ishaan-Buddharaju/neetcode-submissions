"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # input: List[Interval]
        # output: boolean
        # intervals min length: 0
        # - if len 0 return true
        # all intervals have start less than end
        if len(intervals) < 2: 
            return True
        intervals.sort(key=lambda x: (x.start, x.end)) # O(nlogn)
        for i in range(len(intervals) - 1): 
            curr = intervals[i]
            next = intervals[i + 1]
            if  next.start < curr.end:
                return False

        return True