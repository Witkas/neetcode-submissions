# [
#     ["1","0","1","0","0"],
#     ["1","0","1","1","1"],
#     ["1","1","1","1","1"],
#     ["1","0","1","1","1"]
# ]
# ROWS = 4, COLS = 5
# dp = [
#         [0,0,0,0,0,0],
#         [0,0,0,0,0,0],
#         [0,0,0,0,0,0],
#         [0,0,0,0,0,0],
#         [0,0,0,0,0,0],
# ]

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = 0
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if matrix[r][c] != "0":
                    right = dp[r][c+1]
                    bottom = dp[r+1][c]
                    diag = dp[r+1][c+1]
                    dp[r][c] = 1 + min(right, bottom, diag)
                    res = max(res, dp[r][c])
        
        return res * res