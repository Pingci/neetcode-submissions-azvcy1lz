class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited):
            visited.add((r, c))
            
            directions = [
                (0,1),
                (1,0),
                (-1,0),
                (0, -1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and 0 <= nc < cols
                    and heights[nr][nc] >= heights[r][c]
                    and (nr, nc) not in visited):
                    dfs(nr, nc, visited)

        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols - 1, atl)

        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows - 1, c, atl)

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))

        return res
            
                


