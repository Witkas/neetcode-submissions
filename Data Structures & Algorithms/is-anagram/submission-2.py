

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}

        if len(s) != len(t):
            return False

        for letter in s:
            if letter in d1:
                d1[letter] += 1
            else:
                d1[letter] = 1

        for letter in t:
            if letter in d2:
                d2[letter] += 1
            else:
                d2[letter] = 1

        for k in d1:
            if k in d2:
                if d1[k] != d2[k]:
                    return False
            else:
                return False       
        
        return True