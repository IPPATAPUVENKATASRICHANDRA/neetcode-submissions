class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def dfs(i,j,st_w):
            
            if st_w==len(word):
                return True

            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False

            if board[i][j]!=word[st_w]:
                return False

            temp=board[i][j]
            board[i][j]='#'
            res=(dfs(i+1,j,st_w+1) or dfs(i-1,j,st_w+1) or dfs(i,j+1,st_w+1) or dfs(i,j-1,st_w+1))
            board[i][j]=temp

            return res
    
        for i in range(len(board)):
            for j in range(len(board[0])):
            
                if dfs(i,j,0):
                    return True
        
        return False