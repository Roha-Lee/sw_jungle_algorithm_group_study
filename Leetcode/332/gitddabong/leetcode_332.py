class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # 책에 있는 코드인데, 그리디로 접근.
        # 왜 이 코드로 정확한 답이 나올 수 있는지에 대한 이해가 부족함.

        graph = collections.defaultdict(list)
        
        # print(sorted(tickets))
        # 알파벳 순으로 정렬해서 인접 리스트에 삽입
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        # print(graph)
        
        # 길은 있어야 되는데, 그 중에서 가능하면 알파벳 순으로 가라.
        
        route = []
        def dfs(a):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
            
        dfs('JFK')
        
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]
