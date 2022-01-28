class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # k부터 n까지 가는데 걸리는 시간 리턴, 불가능시 -1 리턴
        
        # 다익스트라
        dict = collections.defaultdict(list)
        
        # 인접리스트(입력받음)
        for v1, v2, cost in times:
            dict[v1].append((cost, v2))
            
        # 최솟값 저장할 리스트
        maxc = float('inf')
        min_cost = [maxc for i in range(n+1)]
        
        # 힙선언+초깃값 push
        def Dijkstra(k):
            min_cost[0] = 0 # 0번째 인덱스에는 노드가 없으니까 0으로 세팅
            min_cost[k] = 0 # 시작위치->시작위치 거리는 0이니까
            heap = [[0, k]]
            
            while heap:
                # heappop 최솟값 pop
                cost2, node = heapq.heappop(heap)
                if cost2 <= min_cost[node]:
                    for next in dict[node]:
                        # 최솟값 갱신
                        if cost2+next[0] < min_cost[next[1]]:
                            min_cost[next[1]] = cost2+next[0]
                            # 현재 만난 인접노드들 새로 push
                            heapq.heappush(heap, [cost2+next[0],next[1]])
        
        Dijkstra(k)
        print(min_cost)
        
        if max(min_cost) == float('inf'):
            return -1
        else: # 모든 n개 노드가 신호를 수신하는 데 걸리는 시간을 반환
            return max(min_cost)
                
                
                
                