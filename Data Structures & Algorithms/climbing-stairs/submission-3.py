class Solution:
    # 1 2 3 4 5
    # 3 2 2 1 1
    # 1 -> 1
    # 2 -> 2
    # 3 -> 3
    # 4 -> 5
    def climbStairs(self, n: int) -> int:
        prev, cur = 0, 1
        for i in range(n):
            prev, cur = cur, prev + cur
        return cur
        