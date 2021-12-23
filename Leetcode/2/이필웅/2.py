# LeetCode 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/


# 풀이 1번 - 자료형 변환
# 시간복잡도 O(N), Runtime : 72ms(55.34%) Memory Usage : 14.5MB(11.72%)
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # 리스트 거꾸로 만드는 함수
    def reverseList(self, head):
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev

    # 리스트에 벨류값 넣는 함수
    def toList(self, node): 
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    # 역순으로 된 연결리스트 생성하는 함수
    def toReversedLinkedList(self, result):
        prev: ListNode = None
        for i in result:
            node = ListNode(i)
            node.next = prev
            prev = node
            
        return node
    
    # a,b 두개의 값 합쳐서 역순으로 연결리스트 만드는 함수
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        
        return self.toReversedLinkedList(str(resultStr))

# 풀이 2 - 전가산기(?)
# 설명 필요함.

# 시간복잡도 O(N) Runtime : 68ms(75.55%) Memory Usage : 14.4MB(45.45%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
                
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next