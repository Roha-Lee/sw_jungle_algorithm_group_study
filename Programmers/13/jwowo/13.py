class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        
        total, prev = 0, 0
        
        for i in range(len(s) - 1, -1, -1):
            current = roman[s[i]]
            if current >= prev:
                total += current
            else:
                total -= current
                
            prev = current
            
        return total