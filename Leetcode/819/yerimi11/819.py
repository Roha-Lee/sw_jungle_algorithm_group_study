import collections
import re

# class Solution(object):
#     def mostCommonWord(self, paragraph, banned):
#         """
#         :type paragraph: str
#         :type banned: List[str]
#         :rtype: str
#         """
#         # 카운트에 같은 단어 횟수 세서 가장 많은 카운트인 단어 출력
#         # if 금지된 단어이면 카운트 안함. 금지된 단어 리스트에서 pop하면?
#         # 구두점 무시. 단어와 붙어있으면 단어만 셈 <- ??
        
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph) 
#                 .lower().split()
#                     if word not in banned]
        
#         counts = collections.Counter(words)
#         print(counts)
#         return counts.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = [word for word in re.sub(r'[^\w]', ' ', paragraph) 
        .lower().split()
            if word not in banned]
        # for word in words:
        #     if word in banned:
        #         continue

counts = collections.Counter(words)
print(counts.most_common(1)[0][0]) # 1 빼도 돌아가지만 1을 써줘야 속도가 훨 빨라짐

