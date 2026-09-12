class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ones=[]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    ones.append((i,j))
        
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return
            
            if grid[i][j]!="1":
                return 
            
            if grid[i][j]=='1':
                grid[i][j]='#'
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        cnt=0
        for o in ones:
            r,c=o
            if grid[r][c]=='1':
                cnt+=1
                dfs(r,c)
        
        return cnt

