class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        oned=list()
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                    oned.append((i,j))
        
        
        def dfs(r,c):

            if 0>r or r>=len(grid) or 0>c or c>=len(grid[0]):
                return 
            
            if grid[r][c]!='1':
                return
            
            grid[r][c]=-1

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    cnt+=1
                    dfs(i,j)

        return cnt