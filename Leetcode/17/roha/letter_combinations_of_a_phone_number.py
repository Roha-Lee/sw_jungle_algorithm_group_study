class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        hash_table = {
            '2':['a','b','c'], 
            '3':['d','e','f'], 
            '4':['g','h','i'], 
            '5':['j','k','l'], 
            '6':['m','n','o'], 
            '7':['p','q','r','s'], 
            '8':['t','u','v'], 
            '9':['w','x','y','z']
        }
        result = []
        def dfs(temp, didx):
            if len(digits) <= didx:
                result.append("".join(temp))
                return
            for idx in range(len(hash_table[digits[didx]])):
                temp.append(hash_table[digits[didx]][idx])
                dfs(temp, didx+1)
                temp.pop()
        dfs([], 0)
        return result