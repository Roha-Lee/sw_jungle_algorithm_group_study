class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit(): # isdigit() : 숫자여부 판별 / 0번째는 식별자니까 split 후 1부터 봄.
                digits.append(log)
            else:
                letters.append(log)
                
        # 문자열이 앞에 오도록 출력해야함, 문자열 정렬하기 (숫자열은 입력한 순서로 출력)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        # x.split()[1:] : 문자열 0번째는 항상 ab1같이 소문자+숫자 형태인 식별자니까 1번째 일반 소문자부터 정렬
        # x.split()[0]  :  ㄴ 정렬 우선순위 아님
        
        return letters + digits