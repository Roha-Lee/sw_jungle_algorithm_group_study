# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy_head = ListNode()
        dummy_head.next = head
        curr = dummy_head
        
        for _ in range(left - 1):
            curr = curr.next
        
        before_start, end_node = curr, curr.next
        curr = curr.next
        
        stack = []
        for _ in range(right - left + 1):
            stack.append(curr)
            curr = curr.next
        
        while stack:
            node = stack.pop()
            before_start.next = node
            before_start = before_start.next
        before_start.next = curr
        return dummy_head.next
        
        
        