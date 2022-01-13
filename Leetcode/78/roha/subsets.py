class Solution:        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        def dfs(idx, temp):
            result.append(temp[:])
            for i in range(idx, len(nums)):
                temp.append(nums[i])
                dfs(i+1, temp)
                temp.pop()
        dfs(0, [])
        return result
            