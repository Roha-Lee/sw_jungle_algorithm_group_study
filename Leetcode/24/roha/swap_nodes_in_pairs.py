class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return
        odd = head 
        even = head.next 
        result = ListNode()
        head = result
        while odd and even and odd.next and even.next:
            result.next, even = even, even.next.next
            result = result.next
            result.next, odd = odd, odd.next.next
            result = result.next
            
        if even:
            result.next = even
            result = result.next 
        
        if odd:
            result.next = odd
            result = result.next
        result.next = None
            
        return head.next