class Solution:
    def dfs(self, temp, result):
        if sum(temp) > self.target:
            return 
        elif sum(temp) == self.target:
            result.append(temp[:])
            return 

        for i in range(len(self.candidates)):
            if not temp or(temp and temp[-1] <= self.candidates[i]):
                temp.append(self.candidates[i])
                self.dfs(temp, result)
                temp.pop()
        
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates, self.target = sorted(candidates), target 
        result = []
        self.dfs([], result)
        return result 
        
        
        