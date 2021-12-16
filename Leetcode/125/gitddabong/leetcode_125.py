import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 실행 시간 32ms
        s = s.lower()       # 입력받은 문자열에서 대문자를 모두 소문자로 변경
        s = re.sub('[^a-z0-9]', '', s)  # 문자열에서 소문자, 숫자를 제외한 모든 문자를 ""로 대치.
        return s == s[::-1] # 역순으로 바꾸기 전과 후의 문자열을 비교해서 True, False 출력
        
        
        # 실행 시간 424ms
#         alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)] + [str(x) for x in range(10)]
        
        
#         pure_s = ""
#         for char in s:
#             # 알파벳 소문자나 숫자인 경우
#             if char in alphabet:
#                 pure_s += char
#             # 알파벳 대문자인 경우
#             elif char.lower() in alphabet:
#                 pure_s += char.lower()
                
#             else:
#                 continue
        
#         rv_pure_s = pure_s[::-1]
        
#         if pure_s == rv_pure_s:
#             return True
#         else:
#             return False