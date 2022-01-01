# 328. Odd Even Linked List
[문제 링크](https://leetcode.com/problems/odd-even-linked-list/)

# 문제 요구 조건 
- 홀수 번째 노드를 전부 모으고 짝수 번째 노드를 전부 모은 다음 홀수번째 -> 짝수번째로 나오게 만들자.

# 제한 조건 
- O(1) space complexity, O(N) time complexity로 풀자.
- n은 연결리스트의 노드의 개수 
- `0 <= n <= 10^4`
- `-10^6 <= Node.val <= 10^6`

# 풀이 
- odd에 head를 넣고 even에는 head.next를 넣는다. 
- 마지막에 연결해주기 위해 even_start를 저장해준다. 
- odd.next와 even.next가 있는 동안 반복문을 돌면서 
    - odd.next에 even.next를 넣어준다. 
    - odd를 다음 odd로 옮겨준다. 
        - odd가 더이상 없으면 여기서 반복문 탈출
    - even.next에 odd.next를 넣어준다. 
    - even을 다음 even으로 옮긴다. 
- 마지막으로 odd끝과 even_start를 이어준다. 
# 시간복잡도
- O(1) space complexity, O(N) time complexity로 풀자.
 