class Solution:
    # "zxyzxy"
    # "x"
    # "dvdf"
    # ['d'] res = 1 r = 1
    # ['d', 'v'] res = 2 r = 2
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = r = 0
        letters = set()
        while r < len(s):
            prevLen = len(letters)
            letters.add(s[r])
            if len(letters) > prevLen:
                res = max(res, len(letters))
                r += 1
            else:
                l += 1
                r = l
                letters = set()
        return res
