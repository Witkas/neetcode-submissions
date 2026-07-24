class Solution:
    # ABAA
    # l = r = 0
    # {A: 1} -> 1 - 1 < 0 -> true -> res = 1
    # l = 0, r = 1
    # {A: 1, B: 1} -> 2 - 1 <= 0 -> false -> {A: 0, B: 1}
    # l = 1, r = 2
    # {}
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
