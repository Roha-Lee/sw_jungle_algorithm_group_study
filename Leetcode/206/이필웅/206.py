# LeetCode 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# 접근과 풀이방식은 이해가되나 노드구조가 안그려짐;
# 노드구조 그리는게 이해가 잘 안됨 설명 필요.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev

a = Solution().reverseList([1,2,3,4,5])
print(a)