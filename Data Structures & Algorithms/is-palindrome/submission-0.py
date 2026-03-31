class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_no_space = s.lower().replace(' ', '')
        s_no_space = ''.join(c for c in s_no_space if c.isalnum())
        rev_s = s_no_space[::-1]
        print(s_no_space)
        return s_no_space == rev_s