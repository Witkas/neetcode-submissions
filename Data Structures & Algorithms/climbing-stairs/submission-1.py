class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        tmp, res = 1, 1
        for _ in range(2, n+1):
            tmp, res = res, res + tmp

        return res
