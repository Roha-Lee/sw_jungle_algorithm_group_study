class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        best_s, best_e = 0, 0
        for i in range(1, len(s)):
            for s_idx, e_idx in [(i-1, i), (i-1, i+1)]:
                while 0 <= s_idx < len_s and 0 <= e_idx < len_s and s[s_idx] == s[e_idx]:
                    if (e_idx - s_idx > best_e - best_s):
                        best_e, best_s = e_idx, s_idx
                    s_idx -= 1
                    e_idx += 1
        return s[best_s:best_e+1]