# LeetCode 46. Permutations
# https://leetcode.com/submissions/detail/619138115/

# 순열 문제
# itertools 풀이. DFS 풀이 정리 필요.

# Runtime : 36ms(10.34%)
# Memory Usage : 14.4MB(55.69%)

import itertools
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = list(itertools.permutations(nums,n))
        
        return ans