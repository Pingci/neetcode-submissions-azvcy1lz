class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        q = deque()

        # 1) 所有 treasure/gate (0) 入队
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # 2) BFS 扩散最短距离
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if grid[nr][nc] != INF:   # 只扩散到空地
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))