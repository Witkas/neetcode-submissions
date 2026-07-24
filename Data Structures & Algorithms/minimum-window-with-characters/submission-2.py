class Solution:
    # s="OUZODYXAZV"
    # t="XYZ"
    # t_count = {X: 1, Y: 1, Z: 1}
    # need = 3
    #
    # when Z: sub_count = {Z: 1}, have = 1
    # when X ("OUZODYX"): sub_count = {X: 1, Y: 1, Z: 1}, have = 3, res = "OUZODYX"
    # result = "ZODYX", have = 2
    # when ODYXAZ: res = "ODYXAZ" -> "YXAZ"
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        sub_count = defaultdict(int)
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        have = 0
        need = len(t_count.values())
        for r in range(len(s)):
            sub_count[s[r]] += 1
            if s[r] in t_count and sub_count[s[r]] == t_count[s[r]]:
                have += 1
            # Check if we have all required letters
            while have == need and l <= r:
                if res == "":
                    res = s[l:r+1]
                res = res if len(res) < len(s[l:r+1]) else s[l:r+1]
                sub_count[s[l]] -= 1
                if s[l] in t_count and sub_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
            
        return res