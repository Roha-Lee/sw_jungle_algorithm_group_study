# LeetCode 234. Palindrome Linked List
[문제 출처](https://leetcode.com/problems/palindrome-linked-list/)

# 문제
- 연결리스트가 펠린드롬인지 판별하라.

# 접근 방법
## 풀이 1
- 연결 리스트를 순회하여 리스트 / deque 으로 만들어서 첫 인덱스와 마지막 인덱스를 차례로 비교하여 같은지 틀린지를 판별한다.

## 풀이 2
- Runner 기법을 이용한 방법
  - 한번에 한 칸 이동하는 `slow` 포인터, 한번에 두 칸 이동하는 `fast` 포인터를 이용 `fast`와 `slow`의 포인터를 이동한다.
  - 이동하면서 `slow`가 이동하는 노드들을 역순으로 `rev` 연결 리스트로 연결한다. 
  - `fast`가 연결리스트의 마지막에 다다르면 `slow`는 연결리스트의 중간 지점에 도달히고, `rev`는 첫 노드 중간 노드까지 역순으로 연결된 연결 리스트이다.
    - 따라서 `slow`와 `rev`의 연결 리스트의 값을 비교하며, `slow`가 끝에 도달할 때까지 값이 같으면 `True` 아니면 `False`를 반환한다.

# 코드 1
```python
from collections import deque

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = deque([])
        while head:
            arr.append(head.val)
            head = head.next
        
        while len(arr) > 1:
            if arr.popleft() != arr.pop():
                return False
        
        return True
```

# 코드 2
```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            arr, arr.next, slow = slow, rev, slow.next
            
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        return not rev
```