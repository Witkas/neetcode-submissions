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
        for r in range(len(s)): 
            while s[r] in letters:
                letters.remove(s[l])
                l += 1           
            letters.add(s[r])
            res = max(res, len(letters))
        return res
