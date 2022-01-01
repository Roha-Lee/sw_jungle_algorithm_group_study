     
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        head = result
        carry = 0
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = add // 10 
            result.next = ListNode(add % 10)
            l1, l2, result = l1.next, l2.next, result.next
        
        while l1:
            add = l1.val + carry
            carry = add // 10 
            result.next = ListNode(add % 10)
            result = result.next
            l1 = l1.next
        
        while l2:
            add = l2.val + carry
            carry = add // 10 
            result.next = ListNode(add % 10)
            result = result.next
            l2 = l2.next
        if carry:
            result.next = ListNode(carry)
        return head.next 
   