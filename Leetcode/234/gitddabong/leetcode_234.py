# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        nums = deque()
        curr = head
        while curr != None:
            nums.append(curr.val)
            curr = curr.next
        
        while len(nums) > 1:
            if nums.popleft() != nums.pop():
                return False
        
        return True
                
        
