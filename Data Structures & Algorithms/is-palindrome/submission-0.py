class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        s2 = ""
        for c in s:
            if self.isAlphanumeric(c):
                s2 += c
        for i in range(len(s2)):
            if s2[i] != s2[-1-i]:
                return False
        return True

    def isAlphanumeric(self, s: str):
        return ord('a') <= ord(s) <= ord('z') or ord('0') <= ord(s) <= ord('9')
