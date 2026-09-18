class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac, alt = set(), set()

        def dfs(r, c, visit, pre_hei):

            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visit or
                heights[r][c] < pre_hei
            ):
                return

            visit.add((r, c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Left = Pacific, Right = Atlantic
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, alt, heights[r][cols - 1])

        # Top = Pacific, Bottom = Atlantic
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, alt, heights[rows - 1][c])

        res = []

        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in alt:
                    res.append([i, j])

        return res