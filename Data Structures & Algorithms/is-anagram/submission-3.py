

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}

        if len(s) != len(t):
            return False

        for letter in s:
                d1[letter] = 1 + d1.get(letter, 1)
        for letter in t:
                d2[letter] = 1 + d2.get(letter, 1)

        for k in d1:
            if d1[k] != d2.get(k, 0):
                return False

        
        return True