class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = []
        for letter in s:
            if letter.isalnum():
                filtered_str.append(letter.lower())
        len_str = len(filtered_str) 
        max_idx = len_str // 2
        for i in range(max_idx):
            if filtered_str[i] != filtered_str[-i-1]:
                return False
        return True
        