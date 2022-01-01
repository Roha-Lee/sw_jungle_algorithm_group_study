from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, cntr, used = [], Counter(s), set()
        for letter in s:
            cntr[letter] -= 1
            if letter in used:
                continue
            
            while stack and stack[-1] > letter and cntr[stack[-1]]:
                used.remove(stack.pop())
            stack.append(letter)
            used.add(letter)
        return ''.join(stack)
            
            