class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_table = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100, 
            'D':500,
            'M':1000,
            '.':0}
        result = 0
        stack = []
        s += '.'
        for letter in s:
            digit = symbol_table[letter]
            temp = 0
            while stack and stack[-1] >= digit:
                if not temp:
                    temp = stack.pop()
                    continue
                temp -= stack.pop()
            result += temp
            stack.append(digit)
        return result
        