class Solution:
    def dfs(self, temp, result, exist):
        if sum(temp) > self.target:
            return 
        elif sum(temp) == self.target:
            if tuple(sorted(temp)) not in exist:
                result.append(temp[:])
                exist.add(tuple(sorted(temp)))
            return 

        for i in range(len(self.candidates)):
            temp.append(self.candidates[i])
            self.dfs(temp, result, exist)
            temp.pop()
        
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates, self.target = candidates, target 
        result, exist = [], set()
        self.dfs([], result, exist)
        return result 
        
        
        