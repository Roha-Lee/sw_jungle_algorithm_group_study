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
        
        for i in range(left - 1):
            curr = curr.next
        
        before_start, end_node = curr, curr.next
        
        for i in range(right - left):
            temp, before_start.next, end_node.next = before_start.next, end_node.next, end_node.next.next
            before_start.next.next = temp
        return dummy_head.next 
            
        
        