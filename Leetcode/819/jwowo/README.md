# LeetCode 819. Reorder Data in Log Files
[문제 출처](https://leetcode.com/problems/most-common-word/)

# 문제
- 금지된 단어를 제외하고 가장 많이 사용된 단어를 출력하시오.
- 모든 단어는 대소문자 구분이 없으며 소문자의 형태로 반환하시오.

# 접근 방법
- python의 `regular expression`과 `lower()` 메서드를 통해 소문자 알파벳이 아닌 character는 공백으로 바꾼다.
- 단어의 빈도수를 셀 딕셔너리를 생성하고 `banned` 단어가 아닌 경우에만 개수를 카운트한다.
- `max(word_count,key=word_count.get)` 를 통해 딕셔너리의 가장 큰 값을 가지는 키 값을 반환한다.