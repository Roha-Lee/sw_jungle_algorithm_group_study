class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # candidates 숫자 횟수 제한 없이 더해서 target숫자 만들기
        # 뺄셈으로 찾기 ! target - c
        
        result = []
        
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
        
        dfs(target, 0, [])
        return result

            