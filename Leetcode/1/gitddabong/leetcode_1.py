# target을 만들 수 있는 두 페어를 찾는 문제
# 실행시간 3512ms ㅁㅊ; 
# 뭔가 빠른 방법이 있을 것 같다
nums = [2,7,11,15]
target = 9
success_flag = False

idx1 = 0
idx2 = 0

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            idx1 = i
            idx2 = j
            success_flag = True
            break;
    if success_flag:
        break;
print([idx1,idx2])