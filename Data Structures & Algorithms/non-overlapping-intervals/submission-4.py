class Solution:
    # --- --- ---
    # -----------
    #  ----
    #  -----
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        res = 0
        curEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= curEnd:
                curEnd = end
            else:
                res += 1
                curEnd = min(end, curEnd)
        return res
