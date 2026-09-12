class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area=0
        def dfs(i,j):
            nonlocal cur_area
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return 
            
            if grid[i][j]!=1:
                return 
            
            if grid[i][j]==1:
                cur_area+=1
                grid[i][j]='#'
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    cur_area=0
                    dfs(i,j)
                    max_area=max(max_area,cur_area)


        return max_area

                