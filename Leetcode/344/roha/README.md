# 344. reverse string
[문제 링크](https://leetcode.com/problems/reverse-string/)
# 문제 요구 조건 
- 스트링을 뒤집을 것 
- 입력 배열 내부에서 바꿀 것, Extra memory를 O(1)만 사용할 것
- `1 <= s.length <= 10^5`
# 풀이 
- 스트링을 뒤집기 위해 스트링 길이의 절반을 구함
- 0번과 -1번 자리를 바꾸고 1번과 -2번의 자리를 바꾸는 과정을 스트링 길이의 절반까지 반복
# 시간 복잡도
- O(N/2)