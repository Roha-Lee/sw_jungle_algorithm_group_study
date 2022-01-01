from collections import deque

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs = deque()
            
        for letter in s:
            if letter.isalnum():
                strs.append(letter.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
            
        return True