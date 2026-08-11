class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        res = 0
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if matrix[r][c] == "0":
                    continue
                right = dp[r][c+1] if c + 1 < COLS else 0
                bottom = dp[r+1][c] if r + 1 < ROWS else 0
                max_square = min(right, bottom)
                corner = matrix[r+max_square][c+max_square]
                dp[r][c] = 1 + max_square if corner == "1" else max_square
                res = max(res, dp[r][c])
        return res * res