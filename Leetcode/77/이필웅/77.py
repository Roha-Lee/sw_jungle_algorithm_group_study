# LeetCode 77. Combinations
# https://leetcode.com/problems/combinations/

# Runtime : 72ms (0.89%)
# Memory Usage : 15.6MB

# itertools 사용 간단 풀이

import itertools
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        ans = []
        ans += list(itertools.combinations(nums,k))
        
        return ans

# dfs 사용 풀이
# 어렵다. 연산 과정자체가 직관적으로 떠오르지 않음..

class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])
                return
            
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
                
        dfs([],1,k)

        return results

a = Solution2()

print(a.combine(4,2))