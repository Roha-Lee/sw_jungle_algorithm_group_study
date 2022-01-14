# LeetCode 78. Subsets
# https://leetcode.com/problems/subsets/

# 숫자로된 배열이 주어지면 이 배열로 가능한 조합을 리스트 형태로 반환하는 문제.

# Runtime : 50ms(23%)
# Memory Usage : 14.4MB*(78.76%)
import itertools
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(1,len(nums)+1):
            ans = ans+list(itertools.combinations(nums,i))
            
        return ans