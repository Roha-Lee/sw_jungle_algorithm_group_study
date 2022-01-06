import math
def solution(progresses, speeds):
    answer = []
    stack = []
    max_req_day = 0
    for pr, sp in zip(progresses, speeds):
        req_day = math.ceil((100 - pr) / sp)    
        if not stack:
            max_req_day = req_day
        if req_day > max_req_day:
            answer.append(len(stack))
            stack = [req_day]
            max_req_day = req_day
            
        else:
            stack.append(req_day)
        
    if stack:
        answer.append(len(stack))
    return answer