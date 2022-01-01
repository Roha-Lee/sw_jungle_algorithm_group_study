# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
class Solution:
    def _reverse(self, curr, prev = None):
        if curr.next is None:
            curr.next = prev
            return curr
        
        head = self._reverse(curr.next, curr)
        curr.next = prev
        return head
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        return self._reverse(head)