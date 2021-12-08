# 5. longest palindromic substring
[문제 링크](https://leetcode.com/problems/longest-palindromic-substring/)
# 문제 요구 조건 
- 주어진 스트링에서 가장 긴 팰린드롬인 substring을 찾는 문제 
# 제한
- 1 <= s.length <= 1000
- s는 숫자와 영문만을 포함
# 풀이 
## Sliding window 풀이
1. 2칸짜리 윈도우와 3칸짜리 윈도우를 준비한다. 
    - 2칸짜리 윈도우는 짝수개의 팰린드롬을 찾기 위한 것이고 
    - 3칸짜리 윈도우는 홀수개의 팰린드롬을 찾기 위한 것이다. 
2. 한칸씩 오른쪽으로 이동하면서 각각 2, 3길이의 팰린드롬을 만나면 그 위치에서 좌우로 한칸씩 확장해가면서 그 위치에서 가장 긴 팰린드롬을 찾는다. 
3. 가장 긴 팰린드롬을 반환한다. 
## 시간복잡도 
> O(N^2)
- 윈도우를 슬라이딩하는 길이 N
- 한 칸 씩 확장하면서 비교 연산 수행 N//2
- 시간 복잡도 N * N // 2 -> N^2
## DP 풀이
- 2차원 DP table을 선언해 준다. 
![DP table](https://user-images.githubusercontent.com/82917798/145229936-8bd90c69-f643-4c36-a0f3-56a5dd7b2893.jpeg)
- 짝수개의 팰린드롬을 고려하기 위해 2개짜리 역시 초기화 해준다. 
- DP[i][j] = 2 **(if s[i] == s[j] j-i == 1)**
- DP[i][j] = DP[i+1][j-1] + 2 **(if s[i] == s[j])**
- DP[i][j] = max(DP[i+1][j], DP[i][j-1]) **(if s[i] != s[j])**

## 시간 복잡도 
- O(N(N+1)/2)
- O(N^2)