

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = max(piles)
        while low <= high:
            m = (low + high) // 2
            time_needed = 0
            for p in piles:
                time_needed += math.ceil(p / m)
            if time_needed > h:
                low = m + 1
            else:
                res = min(res, m)
                high = m - 1
        return res