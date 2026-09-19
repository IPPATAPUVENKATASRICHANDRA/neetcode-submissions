class Solution:
    def solve(self, board: List[List[str]]) -> None:


        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        open_safe = set()

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return

            if board[i][j] != 'O':
                return

            if (i, j) in open_safe:
                return

            open_safe.add((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Start DFS only from border O's
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)

        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)

        # Convert only unsafe O's
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i, j) not in open_safe:
                    board[i][j] = 'X'
        

