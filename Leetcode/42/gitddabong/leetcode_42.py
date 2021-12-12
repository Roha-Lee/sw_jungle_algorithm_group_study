# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]

# stack = []
# volume = 0

# for c_dist in range(len(height)):
#     c_height = height[c_dist]
#     # 변곡점을 만나는 경우
#     while stack and c_height > height[stack[-1]]:
#         # 스택에서 꺼내기
#         top = stack.pop()   # 이전 위치의 인덱스 (이전 위치의 높이에 사용)
        
#         if not len(stack):
#             break;

#         distance = c_dist - stack[-1] - 1   # 거리 = 현재 인덱스 - 스택의 top의 인덱스 - 1
#         waters = min(c_height, height[stack[-1]]) - height[top] # 현재 높이와 스택 top의 높이 - 직전 높이

#         volume += distance * waters # 넓이 = 너비 * 높이
    
#     stack.append(c_dist)

# print(volume)



height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
# 에서 오답 발생

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
water = 0

stack = []
for c_dist in range(len(height)):
    c_height = height[c_dist]
    l_height = 0

    while stack and stack[-1][1] <= c_height:
        p_dist, p_height = stack.pop()
        
        h = min(c_height, p_height) - l_height
        d = c_dist - p_dist - 1
        water += h * d

        l_height = p_height
    
    if stack and stack[-1][1] > c_height:
        p_dist = stack[-1][0]
        p_height = stack[-1][1]

        h = min(c_height, p_height) - l_height
        d = c_dist - p_dist - 1
        water += h * d

    stack.append((c_dist, c_height))

print(water)