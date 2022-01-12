from collections import defaultdict, deque
class Solution:
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(deque)
        
        for src, dst in sorted(tickets):
            graph[src].append(dst)
            
        result = []
        def dfs(curr):    
            while graph[curr]:
                dfs(graph[curr].popleft())
            result.append(curr)

        dfs("JFK")    
        return result[::-1]
            