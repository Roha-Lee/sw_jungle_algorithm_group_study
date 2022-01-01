class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        p_open = set(pair.values())
        for letter in s:
            if letter in p_open:
                stack.append(letter)
                continue

            if not stack or not stack[-1] == pair[letter]:
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True

