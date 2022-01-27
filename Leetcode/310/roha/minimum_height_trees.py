from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0]
        graph = defaultdict(set)
        for src, dst in edges:
            graph[src].add(dst)
            graph[dst].add(src)
        next_q, q = deque(), deque()
        
        
        for node in graph:
            if len(graph[node]) == 1:
                next_q.append(node)
        result = None
        while q or next_q:
            if next_q:
                result = list(next_q)
            q, next_q = next_q, q
            while q:
                curr = q.popleft() # 0 2 3
                for nb in graph[curr]:
                    graph[nb].remove(curr)
                    if len(graph[nb]) == 1:
                        next_q.append(nb)
        return result 