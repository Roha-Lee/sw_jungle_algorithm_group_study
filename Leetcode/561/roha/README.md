# 561. Array Partition 1
[문제 링크](https://leetcode.com/problems/array-partition-i/)

# 문제 요구 조건 
- 주어진 nums를 두 파티션으로 나누어서 순서대로 `(ai, bi)`로 쌍을 이루었을때 `min(ai, bi)`의 합을 최소로 만들자. 
# 제한 조건 
- `n <= 10^4`
- `nums.length == 2*n`
- `-10^4 <= nums[i] <= 10^4`

# 풀이 
1. nums[i]가 주어진 범위 내의 정수이므로 계수 정렬로 정렬할 수 있다.
2. 정렬한 후 작은 값 부터 한칸씩 건너뛰고 더하면 된다. 
    - 작은 값끼리 짝짓는 것이 최적해이기 때문. 
# 시간 복잡도 
- 계수정렬: O(N)