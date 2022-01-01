# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        nums = []
        curr = head
        while curr != None:
            nums.append(curr.val)
            curr = curr.next
            
        nums.reverse()
        curr = head
        i = 0
        while curr != None:
            curr.val = nums[i]
            curr = curr.next
            i += 1
            
        return head