# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2): # 연결리스트의 맨 앞 노드 하나. l1 = 2
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode() # 결과값을 넣을 새 노드 하나 만듦, 디폴트값 val = 0 들어가있음, 헤드로 쓸 예정
        curr = node
        carry = 0
        
        while l1 or l2 or carry:
            temp = 0
            curr.next = ListNode() # 또 새 노드 만들고 이음
            
            if l1:
                temp += l1.val
                l1 = l1.next
                
            if l2:
                temp += l2.val
                l2 = l2.next
                
            temp += carry
            curr = curr.next
            
            if (temp < 10):
                curr.val = temp
                carry = 0
            else:
                carry, temp = temp // 10, temp % 10 
                # divmod 함수 로직이랑 같음 => carrr, temp = divmod(temp+carry, 10)
                curr.val = temp
                
        return node.next