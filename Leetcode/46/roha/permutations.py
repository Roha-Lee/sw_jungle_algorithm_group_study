class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        result = []
        def dfs(temp):
            if len(temp) == len(nums):
                result.append(temp[:])
                return 
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    temp.append(nums[i])
                    dfs(temp)
                    visited[i] = False
                    temp.pop()
        dfs([])
        return result
            