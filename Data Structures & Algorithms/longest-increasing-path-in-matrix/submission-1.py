class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        

        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        val=0
        mem={}
        def helper(r,c,prev_val):   

            if r<0 or c<0 or r>=len(matrix) or c>=len(matrix[0]):
                return 0
            if matrix[r][c]<=prev_val:
                return 0
            
            if (r,c,prev_val) in mem:
                return mem[(r,c,prev_val)]

            ans=1

            for dr,dc in dirs:

                nr = r + dr
                nc = c + dc

                ans = max(ans, 1 + helper(nr, nc, matrix[r][c]))
                mem[(r,c,prev_val)]=ans

            return mem[(r,c,prev_val)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val=max(val,helper(i,j,float('-inf')))

        return val

