# LeetCode 316. Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/

# 중복된 문자를 제외하고 사전식 순서로 나열하는 문제

# 스택 활용 풀이 방법
# Runtime : 73ms(9.92%)
# Memory Usage : 14.2MB(91.52%)
import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # counter = 문자 알파벳 단위로 갯수 세줌
        # stack = 정답 배열
        counter, stack = collections.Counter(s), []

        for str in s:
            counter[str] -=1
            if str in stack: continue

            while stack and str < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(str)

        return ''.join(stack)
        
a = Solution()
print(a.removeDuplicateLetters('cbacdcbc'))