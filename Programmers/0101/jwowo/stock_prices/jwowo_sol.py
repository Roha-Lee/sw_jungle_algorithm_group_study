def solution(prices):
    stack = []
    answer = [0] * len(prices)
    
    for price_idx, price in enumerate(prices):
        if not stack:
            stack.append((price_idx, price))
            continue
            
        while stack and stack[-1][1] > price:
            out = stack.pop()
            answer[out[0]] = price_idx - out[0]
        
        stack.append((price_idx, price))
        
    n = len(prices) - 1
    
    while stack:
        stack_idx, stack_price = stack.pop()
        answer[stack_idx] = n - stack_idx
    
    return answer