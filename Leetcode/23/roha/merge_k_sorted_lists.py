# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        idx = 0
        for lst in lists:
            while lst:
                heappush(q, (lst.val, idx, lst))
                lst = lst.next
                idx += 1
        result = ListNode()
        start = result
        while q:
            _, _, result.next = heappop(q)
            result = result.next
        return start.next
        