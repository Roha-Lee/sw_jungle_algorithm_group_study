 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # 인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.
        curr = head
        cnt = 1
        nums = []
        while curr:
            if left <= cnt <= right:
                nums.append(curr.val)
            
            curr = curr.next
            cnt += 1
            
        nums.reverse()
        curr = head
        cnt = 1
        while curr and nums:
            if left <= cnt <= right:
                curr.val = nums.pop(0)
            
            curr = curr.next
            cnt += 1
            
        return head        
    
        # 공간복잡도 O(n) (리스트만듦)
        # 시간복잡도 O(2n) = O(n)