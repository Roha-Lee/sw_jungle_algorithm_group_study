# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # 2 4 3
        # 5 6 4 를 각 자리씩 더해서 새로운 링크드리스트를 만들어서 출력하면 되는 문제.
        # 7 0 8
        
        # 전가산기라는 말이 나와서 어려워보일 수 있는데,
        # 실제로 우리가 덧셈을 할 때도 각 자리수를 더할 때 10을 넘어가면 다음 수에 1을 더하니까
        # 각 자리수를 더하면서 그 다음 수에 1을 더하는 것(carry)를 계산에 추가해준 것 뿐.
        
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
                
            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
            
        return root.next
        

        # String으로 변환해서 풀다 syntax error 뜬 실패작
#         num1_li = []
#         curr = l1
#         while curr:
#             num1_li.append(str(curr.val)
#             curr = curr.next

#         num2_li = []
#         curr = l2
#         while curr:
#             num2_li.append(str(curr.val)
#             curr = curr.next

#         num1 = int("".join(num1_li.reverse()))
#         num2 = int("".join(num2_li.reverse()))

#         num = num1 + num2
#         num_list = list(str(num))

#         result = curr = ListNode(int(num_list[0]))
#         curr = curr.next
#         for _num in num_list[1:]:
#             curr.val = int(_num)
#             curr = curr.next

#         return result
        
        