class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(temp, target, l_idx = 0):
            if target < 0:
                return
            
            elif target == 0:
                result.append(temp[:])
                return
            
            for i in range(l_idx, len(candidates)):
                num = candidates[i]
                temp.append(num)
                dfs(temp, target - num, i)
                if temp:
                    temp.pop()
        
        
        result = []
        temp = []
        dfs(temp, target)
        return result