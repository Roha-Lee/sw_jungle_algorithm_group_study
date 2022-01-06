from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q, used, max_len = deque(), set(), 0
        for letter in s:
            while letter in used:
                used.remove(q.popleft())
            q.append(letter)
            used.add(letter)
            max_len = max(max_len, len(q))
        return max_len