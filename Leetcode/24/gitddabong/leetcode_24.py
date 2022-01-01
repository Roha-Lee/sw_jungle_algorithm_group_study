# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        curr = head
        # 리스트 원소가 0개이거나 1개일 때 종료
        if curr == None or curr.next == None:
            return head
        
        # head를 옮겨주면서 스위치하기 위한 조건문
        else:
            head = curr.next
            
            temp = curr.next.next
            curr.next.next = curr
            curr.next = temp
            
        # 스위치해줄 노드 둘 바로 앞에 curr 위치
        while curr.next and curr.next.next:
            # (1)
            temp = curr.next.next
            # (2)
            curr.next.next = temp.next
            # (3)
            temp.next = curr.next
            # (4)
            curr.next = temp
            # (5)
            curr = temp.next
            
        return head
            