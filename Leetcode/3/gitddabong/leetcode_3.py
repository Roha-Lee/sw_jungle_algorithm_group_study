class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
        
        start = 0       # 투 포인터 중 하나.
        count_li = [0] * len(s)     # 각 인덱스에서 시작해서 만들 수 있는 서로 다른 문자열의 길이를 저장하는 리스트
        q = deque()
        q.append(s[start])
        count_li[0] = 1
        
        for end in range(1, len(s)):
            # 초기에 작성한 코드
            # if s[end] not in q:  # 큐 안에 다음 문자열이 없는 경우 큐에 push, 카운트리스트에 문자열 길이 저장
            #     q.append(s[end])
            # else:               # 큐 안에 이미 받은 문자열이 있는 경우 
            #     while q.popleft() != s[end]:
            #         start += 1
            #     q.append(s[end])
                
            # 위 코드의 최적화 버전
            if s[end] in q:     # 큐 안에 이미 받은 문자열이 있는 경우 큐에서 같은 문자열 만날때까지 지우고 start 포인터도 이동
                while q.popleft() != s[end]:
                    start += 1
                    
            q.append(s[end])
            count_li[start] = len(q)        # 현재 위치에서 end까지 만들 수 있는 문자열의 최대 길이를 리스트에 저장
            
        return max(count_li)