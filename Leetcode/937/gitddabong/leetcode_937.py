# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

logs = ["dig1 8 1 5 1","let17 art can","dig2 3 6","let2 own kit dig","let3 art can"]

# class Solution(object):
#     def reorderLogFiles(self, logs):
#         letters = []
#         digits = []
#         for log in logs:
#             if log.split()[1].isdigit():    # 첫 원소 다음 원소가 숫자면
#                 digits.append(log)      # 숫자 리스트에 삽입
#             else:
#                 letters.append(log)     # 아니면 문자열 리스트에 삽입
#         # 정렬 메인 키 : 식별자 이후 알파벳 순
#         # 정렬 서브 키 : 식별자
#         letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
#         return letters + digits

letters = []
digits = []
for log in logs:
    if log.split()[1].isdigit():    # 첫 원소 다음 원소가 숫자면
        digits.append(log)      # 숫자 리스트에 삽입
    else:
        letters.append(log)     # 아니면 문자열 리스트에 삽입
# 정렬 메인 키 : 식별자 이후의 문자열 알파벳 순
# 정렬 서브 키 : 식별자
letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(letters + digits)

# 그런데 식별자가 3, 17을 넣었으면 3 다음 17의 순서로 나와야 하는 것 아닌가?
# 왜 정답처리가 되나?
# 2번 조건이 있었구나... 사전순