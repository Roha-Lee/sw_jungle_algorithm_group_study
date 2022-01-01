# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head): # head는 연결리스트의 포인터
        """
        :type head: ListNode
        :rtype: bool
        """
        # 연결리스트를 리스트로 받아서 pop으로 비교하자
        head_list = deque()
        curr = head
        
#         # 링크드리스트가 비어있는 경우
#         if head == None:
#             return False

        # C언어 링크드리스트 - 출력 루틴
        # curr = head->next;
        # while (curr != NULL)
        # {
        #     printf("%s\n", curr->data);
        #     curr = curr->next;
        # }

        while curr != None:
            head_list.append(curr.val)
            curr = curr.next

        while len(head_list) > 1: 
            if head_list.popleft() != head_list.pop():
                return False
            
        return True

        # 시간복잡도 while문 n + while 2번째 n/2 더해서 3/2n => 앞 상수 무시. 즉 시간복잡도 (n)
