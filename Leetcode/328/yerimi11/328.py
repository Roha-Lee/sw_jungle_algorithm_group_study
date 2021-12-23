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
        # 홀수번째 노드들이 앞에 오고 그 다음 짝수번째 노드들이 나오도록 해라
        # 공간복잡도 O(1) : 리스트나  다른 연결리스트 만들지말고 갖고있는 걸로 만져서 풀어라, 시간복잡도 O(n)에 풀이하라
        if head is None:
            return None
        odd = head
        even = head.next
        even_head = head.next
        
        while even and odd.next.next: # 두개씩 검사하기 때문에. odd.next.next = even.next
            odd.next = odd.next.next    
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        odd.next = even_head    
        return head