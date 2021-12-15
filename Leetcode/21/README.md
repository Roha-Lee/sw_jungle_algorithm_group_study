21. Merge Two Sorted Lists
[문제 출처](https://leetcode.com/problems/merge-two-sorted-lists/)

# 문제
- 정렬되어 있는 두 연결 리스트가 있을 때, 두 연결 리스트를 합치시오

# 접근 방법
- 두 연결 리스트가 이미 정렬되어있기 때문에 각각의 처음 인덱스부터 노드의 값을 하나씩 비교하여 더 작은 값을 새로운 연결리스트('cuurent`)의 next로 추가한다.
- 두 연결 리스트 중 하나의 연결리스트를 끝까지 다 비교하였다면, 남은 다른 하나의 연결리스트의 남은 노드들을 현재 노드의 다음 (`current.next`)으로 연결한다. 

# 코드 
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = current = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
             
        current.next = list1 or list2

        return answer.next
```