class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        def dfs(_str, depth=0):
            if depth == len(table):
                result.append("".join(_str))
                return
            
            for i in range(len(table[depth])):
                _str[depth] = table[depth][i]
                dfs(_str, depth+1)
                
        
        
        # dict = {"2" : ["a", "b", "c"], 
        #         "3" : ["d", "e", "f"], 
        #         "4" : ["g", "h", "i"], 
        #         "5" : ["j", "k", "i"], 
        #         "6" : ["m", "n", "o"],
        #         "7" : ["p", "q", "r", "s"],
        #         "8" : ["t", "u", "v"],
        #         "9" : ["w", "x", "y", "z"]}
        
        if not digits:
            return []
        
        dict = {"2" : "abc", 
                "3" : "def", 
                "4" : "ghi", 
                "5" : "jkl", 
                "6" : "mno",
                "7" : "pqrs",
                "8" : "tuv",
                "9" : "wxyz"}
        
        table = []      # 탐색용 리스트
        for digit in digits:
            table.append(dict[digit])
            
        print(table)
        
        _str = ["0"] * len(digits)
        result = []     # 결과 저장용 리스트
        dfs(_str)
        
        return result
            