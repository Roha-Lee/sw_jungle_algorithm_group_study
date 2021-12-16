# 15. 3Sum
[문제 링크](https://leetcode.com/problems/3sum/)
# 문제 
- 주어진 배열에서 합을 0으로 만들 수 있는 3개의 원소를 출력하시오

# 문제 접근 방법
- 가장 쉽게 생각할 수 있는 방법은 3중 반복문을 통해 3개의 수의 합이 0이 되는 모든 경우의 수를 확인 하는 방법이다. 하지만 이 방법은 시간 초과가 난다.
- 따라서 투포인터를 이용하여 반복문을 돌면서 조건을 만족하는 경우를 결과에 추가한다.
- 문제의 조건에 따라 중복된 답을 출력하면 안되므로 중복이 되는 예외 처리가 중요하다.

# 코드 
```python
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append((nums[i], nums[left], nums[right]))
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
        return result
```

# 시간 복잡도
  - O(N^2)