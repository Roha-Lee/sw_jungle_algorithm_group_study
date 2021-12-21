# LeetCode 937. Reorder Data in Log Files
[문제 출처](https://leetcode.com/problems/reorder-data-in-log-files/)

# 문제
- 아래 기준에 맞게 로그를 재정렬하기
  - 로그의 가장 앞 부분은 식별자이다.
  - 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
  - 로그의 내용을 기준으로 정렬하고 내용이 동일할 경우, 식별자를 기준으로 정렬한다.
  - 숫자 로그는 입력받은 순서대로 한다.

# 접근 방법
- 입력받은 로그를 문자열 `split()`을 통해 영어 로그인지 숫자 로그인지 확인하여 각각 리스트에 추가한다.
- 영어 로그의 경우 `sort(key = lambda)` 를 이용하여 로그의 내용 기준으로 정렬하고 내용이 같다면, 식별자를 기준으로 정렬한다.
- `영어 로그 리스트 + 숫자 로그 리스트` 로 문자 로그가 숫자 로그보다 먼저 오도록 두 문자열을 합친다.

# 코드
```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        english, digit = [], [] 
        
        for log in logs:
            if log.split()[1].isnumeric():
                digit.append(log)
            else:
                english.append(log)
                
        english.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        
        return english + digit
```