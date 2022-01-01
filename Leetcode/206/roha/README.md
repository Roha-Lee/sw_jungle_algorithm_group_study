# 206. Reverse Linked List
[문제 링크](https://leetcode.com/problems/reverse-linked-list/)
# 문제 요구 조건 
- linked list를 뒤집자. 
# 제한사항 
- linked list의 노드 개수는 `[0, 5000]`
- `-5000 <= Node.val <= 5000`
# 풀이 
1. 반복문을 이용한 풀이 
- stack을 하나 만들고 모든 노드를 stack에 넣어준다. 
- stack을 하나씩 빼면서 역순으로 연결하여 연결 리스트를 만들어준다. 
2. 재귀를 이용한 풀이 
- 마지막 노드까지 이동하다가 마지막 노드에 도착하면 `curr.next = prev`로 노드를 뒤집어준다. 마지막 노드를 반환하여 head에 넣어준다. 
- return하면서 점차 앞의 노드로 이동해 가면서 `curr.next = prev`를 수행하고 마지막에 head를 계속 반환하여 최종적인 return값으로 마지막 노드가 되게 한다. 
# 복잡도 계산 
- O(N)