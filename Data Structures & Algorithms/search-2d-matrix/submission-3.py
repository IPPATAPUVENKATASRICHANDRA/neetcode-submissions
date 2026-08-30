class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r=0
        c=len(matrix[0])-1

        while 0<=r<len(matrix) and 0<=c<len(matrix[0]):
            if matrix[r][c]==target:
                return True
            
            elif matrix[r][c]>target:
                c-=1
            
            else:
                r+=1
        
        return False