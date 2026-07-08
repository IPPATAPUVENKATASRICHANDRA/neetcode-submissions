class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS 
                    and grid[nr][nc] == INF):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))


