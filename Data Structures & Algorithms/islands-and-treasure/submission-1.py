class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r, c])
        
        while queue:
            r, c = queue.popleft()
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = 1 + grid[r][c]
                    queue.append([nr, nc])
