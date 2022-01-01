# 66. Plus One
[문제 링크](https://leetcode.com/problems/plus-one/)
# 문제 요구 조건 
- 주어진 large integer에 1을 더한 값을 구하자.
# 제한사항 
- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits은 leading 0를 포함하지 않는다.`
# 풀이 
> CPU에서 연산될 때는 leading 0을 포함하는 경우가 일반적이므로 마지막 제한사항을 덧붙인게 아닌가 하는 생각이 들었다. 
- carry를 1로 두고 시작한다. 
- Least significant digit에서 Most significant digit으로 이동하면서(역순으로) carry가 있으면 더하고 다시 carry가 발생하는지 체크하여 순차적으로 넣어준다. 
- 결과를 역순으로 반환한다. 

# 시간 복잡도 
- digits의 각 자리수를 한번씩 방문하여 연산하므로 O(N)