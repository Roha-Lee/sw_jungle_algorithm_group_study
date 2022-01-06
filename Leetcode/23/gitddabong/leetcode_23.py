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
        # 이전의 링크드리스트가 2개인 문제처럼 각 노드는 그대로 두되 링크만 바꾸는 방식으로 구현

        root = curr = ListNode(None)  # 값이 없는 헤드 노드
        heap = []  
        
        # 각 연결리스트의 루트를 힙에 저장.
        # 루트를 최소 힙에 넣으면 다른 비교 연산 없이 바로 최솟값을 꺼내올 수 있겠구나
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))   # 힙에 넣는 인자는 value(얘를 기준으로 정렬), 인덱스, 노드 주소
                
        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            value, idx, curr.next = heapq.heappop(heap)   # curr는 결과 리스트의 맨 마지막 노드를 가리키는 주소. pop하면 curr.next에 다음 노드를 연결
            
            curr = curr.next    # 연결된 다음 노드로 포인터 이동
            if curr.next:   # curr의 다음 노드가 있다면 
                heapq.heappush(heap, (curr.next.val, idx, curr.next))   # 다음 노드를 힙에 삽입.
        
        return root.next
        
        
        # 실패작

        # # 지난번 합치면서 정렬하는 문제에서 달라진 것은 리스트가 2개가 아니라 N개인 것.
        # # 그러면 헤드를 배열로 관리하는 것이 좋겠다. 리스트의 개수만큼 가변적이어야 하니까.
        
        # list_heads = []
        # length = len(lists)
        # for i in range(length):
        #     if not lists[i]:
        #         list_heads.append(lists[i])  # 리스트 첫번째 원소의 주소를 저장
        #     else:
        #         list_heads.append(None)
            
        # # 이 리스트들을 하나씩 탐색하면서 수가 작은 노드의 주소값을 큐에 저장하고
        # # 하나씩 popleft() 하면서 노드들을 이어나가면 안될까?
        
        # # 연결리스트들에서 최솟값을 서치할 때 각 헤드의 값을 저장할 리스트를 하나 만들어서
        # # value와 주소값 형태로 튜플을 만들어서 넣으면 접근하기 쉽지 않을까?
        
        # result = []
        # while not None in list_heads:       # 10^4 * 500
        #     # nums = [(0, None)] * length
        #     # dict = {}
        #     min_val = float('inf')
        #     min_addr = None
            
        #     for curr in list_heads: # 10^4
        #         if curr != None:
        #             # nums[i] = (list_heads[i].val, list_heads[i])
        #             # dict = { list_heads[i].val : list_heads[i] }
                    
        #             if min_val >= curr.val:
        #                 min_val = curr.val
        #                 min_addr = curr
            
        #     result.append(min_addr)
        #     list_heads[] = min_addr.next
        
        # if not result:
        #     return None
        
        # l_node = result[0]
        # for node in result[1:]:
        #     l_node.next = node
        #     l_node = node
        # l_node.next = None
        
        # return result[0]
                    
        #     # result.append(dict[min(dict)])
                    
            
            