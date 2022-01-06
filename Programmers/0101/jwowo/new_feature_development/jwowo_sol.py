from collections import deque

def solution(progresses, speeds):
    queue = deque()
    answer = []
    
    for idx, progress in enumerate(progresses):
        remain_percentage = 100 - progress
        
        if remain_percentage % speeds[idx] == 0:
            remain_day = remain_percentage // speeds[idx]
        else:
            remain_day = remain_percentage // speeds[idx] + 1

        queue.append(remain_day)
        
    while queue:
        day = queue.popleft()
        count = 1
        
        while queue and day >= queue[0]:
            queue.popleft()
            count += 1
            
        answer.append(count)
        
    return answer