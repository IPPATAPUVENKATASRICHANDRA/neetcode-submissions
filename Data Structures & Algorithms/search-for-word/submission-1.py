class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
          

        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, idx):
            # found the whole word
            if idx == len(word):
                return True

            # out of bounds
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False

            # character mismatch
            if board[i][j] != word[idx]:
                return False

            # mark visited
            temp = board[i][j]
            board[i][j] = "#"

            # explore neighbors
            found = (
                dfs(i+1, j, idx+1) or
                dfs(i-1, j, idx+1) or
                dfs(i, j+1, idx+1) or
                dfs(i, j-1, idx+1)
            )

            # backtrack
            board[i][j] = temp

            return found

        # try every starting cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
                