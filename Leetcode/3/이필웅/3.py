# LeetCode 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하는 문제.
# 단일 순회로 처리하려 했으나 실패
# 투포인터 활용해서 start값 갱신해가면서 index를 다시금 잡아야함.

# Runtime : 83ms(38.06%)
# Memory Usage : 14.3MB(55.34%)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}   # 해당 문자열의 
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index
        
        return max_length

a = Solution().lengthOfLongestSubstring("abcabcbb")
print(a)