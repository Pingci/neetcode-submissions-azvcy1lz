from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        seen = set([0])
        q = deque([0])

        while q:
            node = q.popleft()
            for nei in g[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)

        return len(seen) == n