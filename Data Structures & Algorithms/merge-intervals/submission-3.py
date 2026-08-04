class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1] = [min(res[-1][0], start), max(res[-1][1], end)]
        return res
            