# LeetCode 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

# target의 값을 candidates의 요소로 조합할 수 있는 경우의 수가 담긴 리스트를 반환하는 문제
# Runtime : 96ms (46.12%)
# Memory Usage : 14.4MB (47.42%)

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        self.Countfuntion(candidates, [], answer, target)
        return answer

    def Countfuntion(self, candidates, current, answer, target):
        if target < 0:
            return
        if target == 0:
            answer.append(current)
            return
        for i in range(len(candidates)): # 0~3까지
            self.Countfuntion(candidates[i:], current + [candidates[i]], answer, target - candidates[i])        

# 책의 풀이

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(sum, i, route):
            if sum < 0:
                return
            if sum == 0:
                ans.append(route)
                return
            
            for i in range(i, len(candidates)):
                dfs(sum - candidates[i],i, route + [candidates[i]])
                
        dfs(target, 0 , [])
        
        return ans