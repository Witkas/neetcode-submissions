class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def recurse(s, i):
            if digits == "":
                return
            if i == len(digits):
                res.append(s)
                return
            for c in digitToLetters[digits[i]]:
                recurse(s + c, i + 1)

        recurse("", 0)
        return res