class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        max_len = max((len(w) for w in words), default=0)

        dp = [False] * (n + 1)
        dp[n] = True  # empty suffix

        for i in range(n - 1, -1, -1):
            # try all end positions up to max_len
            for j in range(i + 1, min(n, i + max_len) + 1):
                if s[i:j] in words and dp[j]:
                    dp[i] = True
                    break

        return dp[0]