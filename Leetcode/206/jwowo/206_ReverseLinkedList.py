# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: 
            return None
        
        current, next_ = head, head.next
        head.next = None
        
        while next_:
            temp = next_
            next_ = next_.next
            temp.next = current
            current = temp
        return current