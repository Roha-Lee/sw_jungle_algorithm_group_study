# LeetCode 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# 풀이법 자체가 노드활용이라 완벽하게 이해는 못한듯.
# 노드 공부 더 필요함

import collections
from typing import Collection, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = List = []

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False 
        
        return True

# 데크 사용 풀이법
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = collections.deque()

        if not head:
            return True
        
        node = head
        while node is not None:
            queue.append(node.val)
            node = node.next

        while len(queue) >1:
            if queue.popleft() != queue.pop():
                return False
        
        return True