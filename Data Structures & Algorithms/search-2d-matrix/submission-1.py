class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # m,n=len(matrix),len(matrix[0])
        # r,c=0,n-1

        # while r<m and c>=0:
        #     if matrix[r][c]>target:
        #         c-=1
        #     elif matrix[r][c]<target:
        #         r+=1
        #     else:
        #         return True
        
        # return False

        m,n=len(matrix),len(matrix[0])
        l,r=0,m*n-1

        while l<=r:
            mid=(l+r)//2
            row,col=mid//n,mid%n
            if target>matrix[row][col]:
                l=mid+1
            elif target<matrix[row][col]:
                r=mid-1
            else:
                return True
        
        return False

