# LeetCode 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

# 일일온도가 입력되있는 리스트 T를 받아서 더 따뜻한 날씨를 위해선 몇일을 더 기다려야 하는지 리스트에 담아 출력해야 하는 문제

# Runtime : 1342ms(24.79%)
# Memory Usage : 25.4MB(48.65%)
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stk = []

        for i, cur in enumerate(temperatures): # 인덱스, 값 형태로 쪼개줌
            while stk and cur > temperatures[stk[-1]]:
                last = stk.pop()
                ans[last] = i - last
            stk.append(i)
            
        return ans

a = Solution()
print(a.dailyTemperatures([73,74,75,71,69,72,76,73]))
