from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])
        q = deque()

        def add_if_O(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == 'O':
                board[r][c] = '#'
                q.append((r, c))

        for c in range(COLS):
            add_if_O(0, c)
            add_if_O(ROWS - 1, c)

        for r in range(ROWS):
            add_if_O(r, 0)
            add_if_O(r, COLS - 1)

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                add_if_O(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
                    