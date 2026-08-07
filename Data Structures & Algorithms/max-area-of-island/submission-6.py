grid = [
  [0,0,0],
  [0,0,0],
  [0,0,0]
]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            if grid[r][c] == 0:
                return 0
            
            curRes = 1
            grid[r][c] = 0
            dirs = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in dirs:
                curRes += dfs(r+dr, c+dc)
            return curRes
        
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        
        return res
