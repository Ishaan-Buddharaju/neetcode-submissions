"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Input: List[Intervals] interval objects
        # Output: min rooms int
        # the min number of rooms is the max number of overlaps
        # since meetings are [start, end) [start end)
        # - overlap is when max(start1, start2) < min(end1, end2) not <=

        '''
        Psuedocode

        map start and end times for number of starts or ends 
        for each invterval map[start]++ map[end]--
        maintain 
        - count
        - maxCount
        sort map
        for each time in map:
            count += map[time] 
            Thus we track how many overlapping meets for each time
            return this max
        '''

        mp = defaultdict(int)
        for meeting in intervals: 
            mp[meeting.start] += 1
            mp[meeting.end] -= 1
        line = sorted(mp) # O(nlogn) time and O(t) space where t is number of unique times in intervals at most intervals * 2
        count = 0
        maxCount = 0
        for time in line: 
            count += mp[time]
            if count > maxCount:
                maxCount = count

        return maxCount

