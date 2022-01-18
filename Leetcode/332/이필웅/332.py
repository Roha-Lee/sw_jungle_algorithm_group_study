# LeetCode 332. Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/

# [from, to]로 구성된 항공권 리스트를 이용해 JFK에서 출발하는 여행 일정을 구하는 문제
# 여러 일정이 겹치는 경우 사전 어휘순 정렬이 필요하다.

# DFS 풀이
# Runtime : 111ms ( 64.36% )
# Memory Usage : 14.9MB ( 47.64% )

from ast import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        return route[::-1]

# 스택 연산으로 큐 최적화 풀이
# Runtime : 76ms ( 10.56% )
# Memory Usage : 14.9 MB ( 47.64% )

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for a, b in sorted(tickets, reverse=True): # 리스트를 역순으로 정렬
            graph[a].append(b)
        
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop()) # pop(0) 하던걸 pop()으로 개선
            route.append(a)

        dfs('JFK')
        return route[::-1]

# 일정 그래프 반복 풀이
# 스택에 하나만 넣고 이 스택에 들어있는 값을 기준으로 graph에서 찾아서 뽑아서 정렬하는 풀이법


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for a, b in sorted(tickets):
            graph[a].append(b)
    
        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        
        return route[::-1]