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
        # 현재의 다음을 전껄로
        # next노드 연결된 걸 끊고 전 노드에 연결시킨다
        curr = head
        prev = None
        
        while curr:
            next = curr.next # 현재(1)의 다음 : 2를 다음노드로 잡고
            curr.next = prev # 이전(None)을 지금의 다음 노드로 연결시킬거임. => 1->None 순서로 거꾸로 연결됨
            
            prev = curr # 현재노드(1)를 다음순서로 넘어가기 위해 이전 노드로 바꾸고
            curr = next # 다음으로 가서(2) 현재노드로 만든다 현재(2) set.
        
            # 그럼 그 다음 2->1 / 3->2 / 4->3 / 5->4 순서로 연결되고
            # 마지막에 5만 리턴하면 쭉 연결되어있으니 5,4,3,2,1 출력됨.
        return prev   
            