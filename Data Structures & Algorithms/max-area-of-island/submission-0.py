class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        cnt_ones=0
        ans=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    cnt_ones+=1
        

        def dfs(r, c):
            if (
                r < 0 or r >= len(grid) or
                c < 0 or c >= len(grid[0]) or
                grid[r][c] != 1
            ):
                return 0

            grid[r][c] = -1

            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )
                

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans=max(ans,dfs(i,j))
        return ans