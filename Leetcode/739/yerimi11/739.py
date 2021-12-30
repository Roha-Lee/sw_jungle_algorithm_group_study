class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
#       스택에 그 날의 온도와 날짜(인덱스)를 같이 넣는다.
#       다음 날의 온도를 받았을 때, 스택에 있는 온도보다 높으면 
#       스택에서 pop하고 날짜의 차이를 result 테이블에 저장한다.
#       스택에 있는 온도보다 낮으면 스택에 추가한다.
        
        # 리스트 초기화
        result = [0] * len(temperatures)
        stack = deque()
        
        for day in range(len(temperatures)):
            temp = temperatures[day]        # temp : 받아온 온도, day : 날짜
            while stack and stack[-1][0] < temp:
                l_temp, l_day = stack.pop()
                result[l_day] = day - l_day
                
            stack.append((temp, day))
        
        return result