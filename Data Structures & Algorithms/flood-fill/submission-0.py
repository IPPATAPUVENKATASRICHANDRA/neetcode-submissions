class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        org_pnt=image[sr][sc]
        if org_pnt==color:
            return image

        def dfs(r, c):
            # Boundary check
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
                return

            # Stop if not the original color
            if image[r][c] != org_pnt:
                return

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr,sc)

        return image