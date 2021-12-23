# 92. Reverse Linked List II
[문제 링크](https://leetcode.com/problems/reverse-linked-list-ii/)
# 문제 요구 조건 
- 연결 리스트를 뒤집는데 왼쪽과 오른쪽 사이의 노드만 역순이 되게 하자. 
# 제한사항 
- list의 노드의 개수는 n이다. 
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`
# 풀이 
1. stack을 이용한 풀이 
- dummy_head를 만들고 next에 head를 넣어준다. 
- curr를 dummy_head에 둔다. 
- curr를 left전까지 이동한 후 curr와 curr.next를 각각 저장한다. 
- right - left + 1개 만큼의 노드가 뒤집히기 때문에 이를 순차적으로 stack에 저장한다. 
    - stack 자료구조의 특성상 FILO이므로 stack에서 pop하여 연결해 주면 노드의 순서를 뒤집을 수 있다. 
- 저장해둔 curr.next뒤에 나머지 노드를 연결해 준다. 

2. one pass풀이
- - dummy_head를 만들고 next에 head를 넣어준다. 
- curr를 dummy_head에 둔다. 
- curr를 left전까지 이동한 후 curr와 curr.next를 각각 저장한다(start, end). 
- right - left번 end노드를 바로 오른쪽 노드와 자리를 바꿔주면 해결할 수 있다. 
  
# 시간복잡도 
- O(N)