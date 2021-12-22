# 561. Array Partition I
[문제 링크](https://leetcode.com/problems/array-partition-i/)
# 문제 
- 원소가 정수이고 개수가 2의 배수인 배열이 주어진다.
- 각 원소들을 두개씩 짝 지어 n개의 pair 를 만들고 각각의 pair에서 작은 값을 더했을 때 그 합이 가장 큰 수를 반환하시오.

# 문제 접근 방법
- nums 리스트 오름차순 정렬한다
  - 문제 요구 조건이 2개씩 짝지은 각각의 pair에서 작은 값을 다 더한 합이므로, 순서는 상관없다. 
- 모든 수는 2개씩 대소비교를 하여 작은 수를 더한다. 문제 요구 조건은 그 두 수들의 합이 가장 크게 하는 것이기 때문에, 큰 수는 큰 수끼리, 작은 수는 작은 수끼리 비교하여 더해야 한다.
- 따라서 주어진 배열 nums를 오름차순 정렬하여 순서대로 index가 2로 나눴을 때 나머지가 0인 값들을 더한다.
  - 정렬된 `nums = [1, 2, 3, 4, 5, 6]` 일 때, 짝은 이루면
  - `(1, 2)(3, 4)(5, 6)` 이 되는데 정렬된 상태이기 때문에 각각의 pair에서 작은 값은 index가 0인 수이다.

# 시간 복잡도
- nums 리스트 원소의 개수만큼 검사
  - O(N)

# 코드 1
```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:        
        nums.sort()
        ans = 0

        for idx, val in enumerate(nums):
            if not idx % 2:
                ans += val
                
        return ans
```

# 코드 2
- `코드 1` 을 한 줄로 작성
```python 
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:        
        return sum(v for i, v in enumerate(sorted(nums)) if not i%2)
```

# 코드 3
- 리스트 컴프리헨션을 이용한 코드 작성
```python 
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:        
        return sum(sorted(nums)[::2])
```