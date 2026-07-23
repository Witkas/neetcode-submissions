class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        s = s.strip().lower()
        while i < j:
            if not self.isAlphanumeric(s[i]):
                i += 1
                continue
            if not self.isAlphanumeric(s[j]):
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def isAlphanumeric(self, s: str):
        return ord('a') <= ord(s) <= ord('z') or ord('0') <= ord(s) <= ord('9')
 