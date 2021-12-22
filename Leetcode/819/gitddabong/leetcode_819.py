# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# paragraph = paragraph.lower()
# paragraph = re.sub('[^a-z0-9\s]', '', paragraph)
# para_list = set(paragraph.split())
# paragraph_list = paragraph.split()
# for ban in banned:
#     # if ban in para_list:
#     para_list.remove(ban)
    
# checklist = [0 for _ in range(len(para_list))]

# for i in range(len(paragraph_list)):
#     if paragraph_list[i] in para_list:


# 정규식 표현의 따옴표 앞에 r을 붙이면 []안의 \등의 특수기호를 단순 문자열이 아닌 특수 문자열로 인식(\w = A-Za-z0-9)

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)  # 정규식으로 [a-zA-Z0-9_] 이외의 것 모두를 공백으로 치환
                    .lower().split()                                # 대문자는 소문자로 바꾸고 문자열 잘라서 리스트로 만들기
                        if word not in banned]                      # 그리고 banned에 포함되지 않은 것만 넣기

        counts = collections.Counter(words)     # 콜렉션의 카운터 객체를 쓰면 리스트의 모든 요소들의 개수를 알 수 있다
        return counts.most_common(1)[0][0]      # most_common : 파라미터로 들어온 개수만큼 카운트가 가장 높은 정렬된 리스트에서 페어를 가져옴.
        # counts.most_common()[0][0] 라고 작성해도 결과는 똑같이 나오는데, 
        # 위의 코드가 실행시간이 절반. 왜?? 
        # 0,0 인덱스로 접근해야 될 전체 데이터량이 많아서 그런가?

        # help(Counter.most_common)