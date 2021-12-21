# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # 두 리스트가 모두 빈 경우
        if not list1 and not list2:
            return list1
        
        # 리스트1이 빈 경우
        elif not list1:
            return list2
        
        # 리스트2가 빈 경우
        elif not list2:
            return list1
                
        result = ListNode()
        list1_p = list1
        list2_p = list2
        
        # 첫 노드가 0이므로 list1과 list2의 첫 값 어느 것 중 하나를 result 첫 노드에 입력
        if list1_p.val <= list2_p.val or not list2_p:
            result.val = list1_p.val
            list1_p = list1_p.next
        elif list1_p.val > list2_p.val or not list1_p:
            result.val = list2_p.val
            list2_p = list2_p.next
        
        # 반복 구문
        curr = result
        while list1_p and list2_p:  # 둘 중 어느 하나라도 None이 되면 반복문 종료
            if list1_p.val <= list2_p.val or not list2_p:
                curr.next = list1_p
                list1_p = list1_p.next
            elif list1_p.val > list2_p.val or not list1_p:
                curr.next = list2_p
                list2_p = list2_p.next
            curr = curr.next
            
        # 어느 한 리스트가 None을 만났을 경우 남은 한 쪽의 리스트를 이어붙이기
        if not list1_p:
            curr.next = list2_p
        elif not list2_p:
            curr.next = list1_p
            
        return result
        