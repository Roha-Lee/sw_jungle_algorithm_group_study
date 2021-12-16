# 238. Product of Array Except Self
[문제 링크](https://leetcode.com/problems/product-of-array-except-self/)
# 문제 요구 조건 
- result[i] = num[i]를 제외한 나머지 원소를 모두 곱한 값인 result를 구하기 
# 제한사항 
- num의 suffix/prefix의 곱은 32bit 정수형을 보장한다.
- O(N) 시간 복잡도 만에 해결할 것 
- 나누기 연산을 사용하지 말 것
- `-30 <= nums[i] <= 30`
- `2 <= nums.length <= 10^5`
# 풀이 
1. prefix product array와 suffix product array를 이용하여 해결 
    - prefix product array의 경우 0부터 i까지의 곱을 나타낸다. 
    - suffix product array의 경우 i부터 끝까지의 곱을 나타낸다. 
    - prefix를 한칸 왼쪽으로(0부터 i-1까지의 곱), suffix를 한칸 오른쪽으로 이동하고(i+1부터 끝까지의 곱) 각 위치를 곱하면 구하고자 하는 리스트를 만들 수 있다.  