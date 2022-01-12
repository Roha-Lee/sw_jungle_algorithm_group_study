class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(curr, temp):
            if len(temp) == k:
                result.append(temp[:])
                return 
            for i in range(curr+1, n+1):
                temp.append(i)
                dfs(i, temp)
                temp.pop()
        result = []
        dfs(0, [])
        
        return result