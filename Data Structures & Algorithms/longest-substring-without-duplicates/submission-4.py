class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 1:
            return 0

        max_len = 1
        l, r = 0, 1
        read_set = set()
        read_set.add(s[l])
        tmp_len = 1
        while r < len(s):
            if s[r] in read_set:
                l = l + 1
                r = l + 1
                read_set = set()
                read_set.add(s[l])
                max_len = max(max_len, tmp_len)
                tmp_len = 1
            else:
                read_set.add(s[r])
                tmp_len += 1
                r += 1

        max_len = max(max_len, tmp_len)
        return max_len
        