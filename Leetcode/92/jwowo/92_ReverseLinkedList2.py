# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # edge case
        if left == right:
            return head
        
        prev = start = ListNode(-501, None)
        current = head
        index = 1      
        
        while current:
            if index < left:
                prev = current

            elif index == left:
                start = current
                
            elif index > left and index <= right:
                prev.next, start.next, current.next = current, current.next, start
                current, start = start, current
                
            index += 1
            current = current.next
            
        while head:
            print(head.val, end=' ')
            head = head.next

    ### 실패 코드