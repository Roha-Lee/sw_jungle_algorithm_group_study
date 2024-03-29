# 937. Reorder data in log files
[문제 링크](https://leetcode.com/problems/reorder-data-in-log-files/)

# 문제 요구 조건 
- 첫번째 단어는 Identifier
- log는 숫자로그, 문자로그가 있다
- 숫자로그의 경우는 주어진 순서 그대로
- 문자로그의 경우는 identifier를 제외한 나머지 단어들의 사전 순서대로 정렬(동일한 경우 identifier를 사전순서)
- 문자로그 -> 숫자로그 순서대로 만들기

# 제한 조건 
- 모든 로그 스트링의 토큰은 공백으로 구분 
- 모든 로그는 identifier와 적어도 하나의 word를 가진다. 
- 로그 데이터는 100개 이하, 각 로그의 길이는 100이하

# 풀이 
1. 숫자로그와 문자로그 구분
    - 적어도 하나의 word를 가진다고 하였으므로 log를 split하였을때 1번 원소를 기준으로 isdigit 스트링 메소드를 이용하여 문자인지 숫자인지 판단하여 따로 저장 
2. 문자로그 정렬 
    - 튜플의 경우 첫 번째 원소를 기준으로 정렬하였을 때 첫번째 원소가 같으면 나머지 원소에 대해 순차적으로 정렬되므로 이 성질을 이용하여 정렬
    - join을 이용하여 다시 원상복구 후 문자로그와 숫자로그 리스트를 더해서 반환 
