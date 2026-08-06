class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue = deque([(r, c)])
                    curRes = 1
                    while queue:
                        nr, nc = queue.popleft()
                        grid[nr][nc] = 0
                        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        for dr, dc in directions:
                            if nr+dr >= 0 and nc+dc >= 0 and nr+dr < rows and nc+dc < cols:
                                if grid[nr+dr][nc+dc] != 0:
                                    queue.append((nr+dr, nc+dc))
                                    curRes += 1
                                    grid[nr+dr][nc+dc] = 0
                    res = max(res, curRes)
        return res
