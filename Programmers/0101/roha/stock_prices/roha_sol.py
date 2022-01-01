def solution(prices):
    answer = [day for day in range(len(prices)-1, -1, -1)]
    stack = []
    
    for idx, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            past_idx, _ = stack.pop()
            answer[past_idx] = idx - past_idx
        stack.append((idx, price))
        
    
    return answer