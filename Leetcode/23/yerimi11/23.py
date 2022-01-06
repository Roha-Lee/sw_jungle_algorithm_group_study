# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 21번과 다른 점 : 21번문제는 연결리스트가 각 리스트로 분리되어있고, 이 문제는 링크드리스트의 헤드들을 리스트로 모아놨다.
        # lists안의 list를 인덱스로 한 번 더 나누면(접근) 되지 않을까?
        # list1, list2를 lists[0] lists[1]로 바꾸면 될 듯 
        #   -> list 갯수를 세서 큰 for문 안에 전체 코드를 돌려야겠네 > 와일문은?? 못쓴다. 삭제완
        # 최종 리턴 값도 result 리스트값 출력이 아니라 연결리스트 값->값 이 나오게 출력해야겠네 다 이어놓은 Head를 출력하면 될 듯
        
        heap = []
        # heapq.heappush(heap, )
        # heapq.heappop(heap)
        result = ListNode()
        
        for i in range(len(lists)): # list[i] : head부터 쭈루룩 들어있으니 헤드의 주소가 됨
            heap = heapq.heappush(heap, (lists[i].val, lists[i]))
        # 맨 처음에 [1, 1, 2]처럼 헤드들이 들어감
        
        while not heap: # 힙이 빌 때 까지
            val, addr = heapq.heappop(heap) # 튜플로 나옴
            result = val
            heap = heapq.heappush(heap, ())
            
            풀다 말음 !
            
            