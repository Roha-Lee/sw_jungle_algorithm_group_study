# LeetCode 328. Odd Even Linked List
[문제 출처](https://leetcode.com/problems/odd-even-linked-list/)

# 문제
- 연결 리스트가 주어질 때 홀수번째 노드 다음에 짝수번째 노드가 오도록 재구성하시오. 
- 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하시오.

# 접근 방법 1
- 홀수번째 노드들을 잇는 홀수 연결리스트 `odd_list` 와 짝수번째 노드들을 잇는 짝수 연결리스트 `even_list` 를 각각 만들고 
- `odd_list` 맨 마지막 노드의 `next` 를 `even_list`의 시작 노드를 연결한다.

# 접근 방법 2
- 홀수번째 노드이면 스킵하고 짝수번째 노드들에 대해서 연결 리스트의 맨 뒤 노드와 연결한다.

# 코드 1
```python
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        odd = odd_head = head
        even = even_head = head.next
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            
        odd.next = even_head
        
        return head
```

# 코드 2
```python
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        temp = end = head
        count = 0
        
        while end.next:
            end = end.next
            count += 1
            
        count = (count // 2) + 1 if count & 1 else count // 2

        while count:
            end.next = temp.next
            temp.next = temp.next.next
            end.next.next = None
            temp = temp.next
            end = end.next
            count -= 1
            
        return head
```