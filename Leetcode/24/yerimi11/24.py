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
        # Example 조건 2
        if (head == None):
            return
        
        curr = head
        next = curr.next
        temp = curr.val
        
        # Example 조건 3
        if (next == None):
            return head
        
        while curr and curr.next: # curr, curr.next가 있을 때 도니까 둘이 없어질 떄 까지(링크드리스트가 끝(None))까지 도착했을 때 까지 돔
            temp = curr.val
            curr.val = next.val
            next.val = temp
            
            curr = next.next
            if (curr == None):
                break # continue는 다음 반복을 진행, break 이 반복문을 멈춘다
            next = curr.next
        return head