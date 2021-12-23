# LeetCode 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# 반복 구조 이용
# Runtime : 40ms(82.85%)
# Memory Usage : 16.3MB(83.42%)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None:
                return None
            
            odd = head
            even = head.next
            even_head = head.next
            
            while even and even.next:
                odd.next, even.next = odd.next.next, even.next.next
                odd, even = odd.next, even.next
                
            odd.next = even_head
            return head