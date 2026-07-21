

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 1)
            countT[t[i]] = 1 + countT.get(t[i], 1)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True