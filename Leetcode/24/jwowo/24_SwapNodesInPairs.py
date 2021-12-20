from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode()
        prev.next = head
        
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            
            prev.next = b
            
            head = head.next
            prev = prev.next.next
        
        return root.next