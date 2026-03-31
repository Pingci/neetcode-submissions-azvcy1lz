class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        n = len(s)

        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        def dfs(start):
            if start == n:
                res.append(part[:])
                return

            for end in range(start, n):
                if is_pal(start, end):
                    part.append(s[start:end + 1])
                    dfs(end + 1)
                    part.pop()

        dfs(0)
        return res