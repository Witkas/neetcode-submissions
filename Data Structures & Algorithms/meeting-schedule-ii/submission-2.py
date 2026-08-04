"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        meeting_count = 0
        res = 0
        sp, ep = 0, 0 # start pointer, end pointer
        while sp != len(intervals) and ep != len(intervals):
            if starts[sp] < ends[ep]:
                meeting_count += 1
                sp += 1
            else:
                meeting_count -= 1
                ep += 1
            res = max(res, meeting_count)
        return res
