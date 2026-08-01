class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, isNewIsland):
            if r == ROWS or c == COLS or r < 0 or c < 0 or grid[r][c] == "0" or (r, c) in visited:
                return
            else:
                visited.add((r, c))
                if isNewIsland:
                    self.res += 1
                dfs(r + 1, c, False)
                dfs(r - 1, c, False)
                dfs(r, c + 1, False)
                dfs(r, c - 1, False)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, True)
        return self.res