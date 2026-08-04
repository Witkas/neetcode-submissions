class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        height, width = m - 1, n - 1
        memo = {(height, width): 1}

        def dfs(m, n):
            if (m, n) in memo:
                return memo[(m, n)]
            if m > height or n > width:
                return 0
            res = dfs(m, n + 1) + dfs(m + 1, n)
            memo[(m, n)] = res
            return res
        
        return dfs(0, 0)
        