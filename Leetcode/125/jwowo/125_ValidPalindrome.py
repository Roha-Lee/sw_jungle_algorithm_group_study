class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_text = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                alpha_text += char.lower()
                
        for i in range(len(alpha_text) // 2):
            if alpha_text[i] != alpha_text[-(i + 1)]:
                return False
            
        print(alpha_text)
        return True