# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         # 사전순 상관 없이 연속되는 문자가 같은 문자만 아니면 문자열로 취급
#         # Hash table -> Dictionary
        
#         # 투 포인터
#         start = 0
#         end = 1
#         if len(s) == 0:
#             return 0
        
#         temp = s[0]                      # 문자열을 저장할 임시 공간. 맨 처음 값을 넣고 시작
#         dict = {len(temp) : len(temp)}   # 해쉬 테이블. {길이 : 문자열}
        
#         while end < len(s): # end 포인터 옮겨준다
#             # 끝에 넣은 새 문자가 중복된 문자이면
#             if s[end] in temp:
#                 start = start + 1
#                 # 딕셔너리(해쉬 테이블)에 저장
#                 temp = s[start]
#                 end = start + 1
#                 temp += s[end]          # 새로 넣은 문자 추가
#                 temp = "".join(list(set(temp)))
#                 dict[len(temp)] = len(temp)  # 딕셔너리 추가 
#                 end += 1
                
#             elif start != 0 or s[end] not in temp: # 새로운 문자이면
#                 temp += s[end]
#                 dict[len(temp)] = len(temp)
#                 end += 1
                
#         return dict[max(dict)]

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 사전순 상관 없이 연속되는 문자가 같은 문자만 아니면 문자열로 취급
        # Hash table -> Dictionary
        
        # 투 포인터
        start = 0
        
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        
        temp = s[0]                      # 문자열을 저장할 임시 공간. 맨 처음 값을 넣고 시작
        dict = {len(temp) : len(temp)}   # 해쉬 테이블. {길이 : 문자열}
        max_len = 0
        for end in range(1, len(s)):
            if s[end] in temp:
                while s[start] != s[end]:
                    start += 1
                start += 1
                temp = s[start:end+1]
            else:
                temp += s[end]
            max_len = max(max_len, len(temp))
        return max_len
#         for end in range(1, len(s)): # end 포인터 옮겨준다
#             # 끝에 넣은 새 문자가 중복된 문자이면
#             if s[end] in temp:
#                 start = start + 1
#                 # 딕셔너리(해쉬 테이블)에 저장
#                 temp = s[start]
#                 end = start + 1
#                 temp += s[end]          # 새로 넣은 문자 추가
#                 set(temp)
#                 dict[len(temp)] = len(temp)  # 딕셔너리 추가    
                
#             elif start != 0 or s[end] not in temp: # 새로운 문자이면
#                 temp += s[end]
#                 dict[len(temp)] = len(temp)
                
#         return dict[max(dict)]