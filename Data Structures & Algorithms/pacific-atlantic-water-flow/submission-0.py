class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac = [[False]*COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue
                if visited[nr][nc]:
                    continue

                if heights[nr][nc] < heights[r][c]:
                    continue
                
                dfs(nr, nc, visited)

        for c in range(COLS):
            dfs(0, c, pac)

        for r in range(ROWS):
            dfs(r, 0, pac)

        for c in range(COLS):
            dfs(ROWS - 1, c, atl)
        for r in range(ROWS):
            dfs(r, COLS - 1, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res