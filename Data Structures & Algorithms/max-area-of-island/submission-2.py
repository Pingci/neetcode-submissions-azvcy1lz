class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0

        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):

            if (r < 0 or r == ROW or c < 0 or c == COL or grid[r][c] == 0):
                return 0 
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            grid[r][c] = 0
            
            area = 0
            for nr, nc in directions:
                if r + nr < ROW and c + nc < COL and grid[r + nr][c + nc] == 1 :
                    area += dfs(r + nr, c + nc)
                    print(area)

            return area + 1


        for i in range(ROW):
           for j in range(COL):
            if grid[i][j] == 1:
                res = dfs(i, j)
                maxArea = max(res, maxArea)

        return maxArea
