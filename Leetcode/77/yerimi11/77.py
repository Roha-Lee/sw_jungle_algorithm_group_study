class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 1~n까지 numbers중에 k개 숫자의 조합
        
        result = []
        self.dfs(range(1, n+1), k, [], result)
        return result
        
    def dfs(self, nums, k, path, result):
        if k == 0:
            result.append(path)
            return
        if len(nums) >= k:
            for i in range(len(nums)):
                self.dfs(nums[i+1:], k-1, path+[nums[i]], result)
        return