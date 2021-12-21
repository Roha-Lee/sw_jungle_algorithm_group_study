class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        
        left = 0
        result = 0
        while left < len(s) :
            if roman[s[left]] > roman[s[left + 1]] :
                result += roman[s[left]]
                left += 1
            else :
                result += roman[s[left+1]] - roman[s[left]]
                left += 2
                
        
        return result
    
    #끝까지 못풀었습니당 ㅠ
