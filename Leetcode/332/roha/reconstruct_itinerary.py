from collections import defaultdict
class Solution:
    def dfs(self, curr, result, flg):    
        if len(result) == len(self.tickets) + 1:
            self.result = result[:]
            return True
        
        for idx, nb in enumerate(self.graph[curr]):
            if not self.visited[curr][idx] and not flg:
                self.visited[curr][idx] = True
                result.append(nb)
                flg = self.dfs(nb, result, flg)
                result.pop()
                self.visited[curr][idx] = False
        return flg
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        visited = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
            visited[src].append(False)
        for node in graph:
            graph[node].sort()

        self.tickets, self.graph, self.visited = tickets, graph, visited
        result = ["JFK"]
        self.dfs("JFK", result, False)    
        return self.result
            