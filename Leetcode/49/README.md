# 49. Group Anagrams
[문제 링크](https://leetcode.com/problems/group-anagrams/)
# 문제 요구 조건 
- anagram끼리 그룹 만들기  
# 제한
- 단어 개수 <= 10^4
- 단어 길이 <= 100
- 단어는 영어 소문자만을 포함 
# 풀이 
1. anagram은 등장하는 글자의 빈도수가 동일하다.
    - Counter를 이용하여 등장하는 글자의 빈도수를 세어준다. 
2. grouping을 위해 dictionary를 사용하려고 하는데, dictionary의 key값으로는 immutable object를 사용해야 한다. 
    - Counter의 `items()` 메소드를 이용하여 key, value쌍으로 이루어진 값들을 받아서 key값으로 sort해주고 immutable로 만들어 주기 위해 tuple로 type casting하였다. 
    - 이 값을 키값으로 하여 group_dict에 word를 값으로 넣었다. 
3. 결과 만들기 
    - group_dict의 value를 가져왔다. 