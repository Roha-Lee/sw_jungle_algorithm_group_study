# 24. Swap Nodes in Pairs
[문제 링크](https://leetcode.com/problems/swap-nodes-in-pairs/)
# 문제 요구 조건 
- `홀수 -> 짝수 -> 홀수 -> 짝수`로 되어있는 리스트를 `짝수 -> 홀수 -> 짝수 -> 홀수`로 바꾸자
# 제한사항
- 리스트의 노드 개수는 0이상 100이하이다.
- `0 <= Node.val <= 100` 
# 풀이 
- 홀수와 짝수를 나누어서 각각 head와 head.next를 넣어준다. 
- dummy head를 만들어주고 짝수를 먼저 연결하고 홀수를 연결하는 것을 반복한다. 
- 남은 노드들을 순서에 맞게 연결해 주고 
- dummy head 다음 노드를 반환해준다.
# 시간 복잡도 
- O(N)
 

