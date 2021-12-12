# 819. Most Common Word
[문제 링크](https://leetcode.com/problems/most-common-word/)

# 문제 요구 조건 
- ban되지 않은 단어들 중에서 가장 빈번하게 등장한 단어 찾기 
- 답의 유일함이 보장됨 
- 적어도 하나의 ban되지 않은 단어가 존재
- 문단은 대소문자를 구별하며, 답은 소문자로 반환

# 제한 조건 
- 문단길이는 1이상 1000이하
- 문단은 영문, 공백, !?',;.으로 구성
- ban은 소문자

# 풀이 
1. 모든 특수문자를 공백으로 바꾸는 과정
    - `'hit the ball,'`의 경우 `ball,`으로 인식되면 안되고 `ball`로 인식되어야함 
    - `hello!roha`의 경우 `hello`, `roha`로 인식되어야 하기 때문에 모든 특수문자를 공백으로 바꿔야함
2. 문단 전부 소문자로 만들어 준 후(lower) 공백으로 split한다. 이때 ban된 단어의 경우 제외한다. 
3. Counter를 이용하여 등장 횟수를 세어주고 Counter의 most_common메소드를 이용하여 빈도가 높은 순으로 만들어 준 후 0번째 원소(가장 빈번한 원소)의 0번째 값(키 값)을 반환한다.

# 정규 표현식으로 대체 
[정규 표현식 위키 링크](https://wikidocs.net/4308)
틈틈히 공부하자..
- `re.sub(src, trg, sentence)`: sentence의 모든 src패턴을 trg로 변경
- `r[^\w]`
    - `\w`: 문자 `a-zA-Z`와 동일
    - `^`: not
    - `r`: 정규표현식 패턴의 시작