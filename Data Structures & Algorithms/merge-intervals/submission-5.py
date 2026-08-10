class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            # Merge
            if cur[1] >= intervals[i][0]:
                cur[1] = max(intervals[i][1], cur[1])
            # Not Merge
            else:
                res.append(cur)
                cur = intervals[i]
        res.append(cur)
        return res