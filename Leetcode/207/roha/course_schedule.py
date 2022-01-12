from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        graph = defaultdict(list)
        inward = defaultdict(int)
        for pre, course in prerequisites:
            graph[pre].append(course)
            inward[course] += 1

        result = []
        q = deque()
        for node in graph:
            if inward[node] == 0:
                q.append(node)
        
        while q:
            curr = q.popleft()
            result.append(curr)
            for nb in graph[curr]:
                inward[nb] -= 1
                if inward[nb] == 0:
                    q.append(nb)

        return len(result) == len(graph.keys())
