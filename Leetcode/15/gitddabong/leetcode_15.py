# 서로 다른 수(인덱스가 다른 수) 를 사용해서 세 수의 합이 0이 되는 페어를 모두 찾아라?

# nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
# # answer  =[[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
# result = []
# nums.sort()

# left = 0
# right = len(nums)-1

# while right-left >= 2:
#     sum = nums[left] + nums[right]
    
#     for i in range(left+1, right):
#         if sum + nums[i] == 0:
#             if [nums[left], nums[i], nums[right]] in result:
#                 continue
#             result.append([nums[left], nums[i], nums[right]])

#     if sum < 0:
#         left += 1
#     else:
#         right -= 1

# print(result)



# nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
# answer  =[[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]

nums = [-1,0,1,2,-1,-4]
result = []
nums.sort()

# 반복문을 왜 이렇게 짰지?
for i in range(len(nums) - 2):  # i = 0 1 2 3
    # 중복된 값 건너뛰기
    if i > 0 and nums[i] == nums[i-1]:
        continue

    # 간격을 좁혀가며 합 sum 계산
    left, right = i+1, len(nums)-1
    # 포인터가 교차할 때까지 반복
    while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            # sum = 0인 경우이므로 정답 및 스킵 처리
            result.append([nums[i], nums[left], nums[right]])

            # 중복된 값이 있을 수 있으니 다음 값이 현재 값과 같으면 포인터 옮기기
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            
            # 같은 숫자들 중에서 끝점까지 왔으니 이제 포인터 옮기기
            left += 1
            right -= 1

print(result)