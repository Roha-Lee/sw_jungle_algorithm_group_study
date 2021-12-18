# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# 노드구조라 진짜 이해가안감. 그냥 리스트구조로 생각하면 로직 구현했는데..
# 노드구조에 진짜 취약함. -> 풀이 물어보기

class Solution:
    def mergeTwoLists(self, list1, list2):
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list1