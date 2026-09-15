class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q=deque()
        dirs=[(0,1),(0,-1),(-1,0),(1,0)]
        mins=0
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
                
        
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < len(grid) and
                        0 <= nc < len(grid[0]) and
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            mins += 1

        return mins if fresh == 0 else -1

