class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        height, width = m - 1, n - 1
        memo = {(height, width): 1}

        def dfs(m, n):
            if (m, n) in memo:
                return memo[(m, n)]
            res = 0
            if m < height:
                res += dfs(m + 1, n)
            if n < width:
                res += dfs(m, n + 1)
            memo[(m, n)] = res
            return res
        
        return dfs(0, 0)
        