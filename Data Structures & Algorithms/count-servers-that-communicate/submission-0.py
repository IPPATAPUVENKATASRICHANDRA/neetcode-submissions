class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
         
        cnt=0
        visit=set()

        def dfs(r, c):
            if (r, c) in visit:
                return
            visit.add((r, c))

            # Check the entire row
            row_has_other = False
            for j in range(len(grid[0])):
                if j != c and grid[r][j] == 1:
                    row_has_other = True
                    break

            # Check the entire column
            col_has_other = False
            for i in range(len(grid)):
                if i != r and grid[i][c] == 1:
                    col_has_other = True
                    break

            if row_has_other or col_has_other:
                nonlocal cnt
                cnt += 1
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visit and grid[r][c]==1:
                    dfs(r,c)
        
        return cnt
