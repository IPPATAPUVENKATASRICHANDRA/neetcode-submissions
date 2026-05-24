class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=len(board)
        c=len(board[0])
        row_check=defaultdict(set)
        col_check=defaultdict(set)
        subblock_check=defaultdict(set)

        for i in range(r):
            for j in range(c):
                if board[i][j]=='.':
                    continue
                
                if (board[i][j] in row_check[i] or board[i][j] in col_check[j] or board[i][j] in subblock_check[(i//3,j//3)]):
                    return False
                
                col_check[j].add(board[i][j])
                row_check[i].add(board[i][j])
                subblock_check[(i//3,j//3)].add(board[i][j])
        
        return True