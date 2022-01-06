# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # 홀수 노드 중 가장 끝 노드를 서치
        curr = head
        length = 1
        end = None          # 맨 뒤의 노드(노드 추가용)
        last_node = None    # 맨 뒤의 노드(종료 조건용)
        while curr:
            if length % 2 == 1:
                end = last_node = curr
            curr = curr.next
            length += 1
        
        # 리스트 길이가 2개 이하면 추가 연산 필요없음.
        if length <= 2:
            return head
            
        curr = head
        cnt = 1
        
        # last_node(종료 조건)를 만나기 전까지 반복
        while curr != last_node:
            if cnt % 2 == 1:
                temp = curr.next
                curr.next = temp.next
                
                temp.next = end.next
                end.next = temp
                end = temp
                cnt += 1
                
            curr = curr.next
            cnt += 1
        
        return head
            
