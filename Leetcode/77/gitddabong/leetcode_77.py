class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        def dfs(temp, l_idx = 0, depth = 0):
            if depth == k:
                result.append(temp[:])
                return
        
            for i in range(l_idx, n):
                temp[depth] = nums[i]
                dfs(temp, i+1, depth + 1)
        
        nums = list(range(1, n+1))
        temp = [0] * k
        result = []
        
        dfs(temp)
        return result