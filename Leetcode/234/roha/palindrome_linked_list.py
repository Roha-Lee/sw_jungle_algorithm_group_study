# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next 
        
        # Reverse
        temp = None
        while slow and slow.next:
            slow.next.next, slow.next, temp, slow = slow, temp, slow.next, slow.next.next
        if slow:
            slow.next = temp
            front, back = head, slow
        else:
            front, back = head, temp
        
        
        while back:
            if back.val != front.val:
                return False
            front, back = front.next, back.next
        return True