# Porgrammers 스택/큐 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

# 문제설명 한글이니까 다시볼때 링크타고 들어가기
# 시간 복잡도 예상 : O(N)

def solution(progresses, speeds):
  # 7, 4, 9
    time = []
    ans = []
    for i in range(len(progresses)):
        last = 100 - progresses[i]
        if last % speeds[i] != 0:
            last = (last // speeds[i]) +1
        else: 
            last //= speeds[i]
        time.append(last)
    
    min = time[0]
    cnt = 1
    for i in range(1,len(time)):
        if min < time[i]:
            ans.append(cnt)
            min = time[i]
            cnt = 1
        else:
            cnt +=1
    ans.append(cnt)
    
    return ans
            