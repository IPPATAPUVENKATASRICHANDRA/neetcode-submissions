class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q=deque()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = 2147483647

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    q.append((i,j))
        
        while q:
            r,c=q.popleft()
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if (0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==INF):
                    grid[nr][nc]=grid[r][c]+1
                    q.append((nr,nc))


       