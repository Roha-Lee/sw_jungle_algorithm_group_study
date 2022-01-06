class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        result = []
        
        for c in s:
            counter[c] -= 1
            
            if c in result:
                continue
            
            while result and c < result[-1] and counter[result[-1]] > 0:
                result.pop()
                
            result.append(c)
            
        return ''.join(result)