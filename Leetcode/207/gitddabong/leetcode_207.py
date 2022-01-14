# 디버깅용 코드

import collections

# visit 리스트에서 값이 0이라면 재귀를 도는 중에는 방문 표시.
# 만약 재귀를 도는 중에 방문한 정점을 만나게 되면(visit[node] == 0) 그 말은 이 그래프에 루프가 있다는 얘기. False 출력
# 리스트를 탐색하면서 더 이상 경로가 없는 경우가 있는데, 이는 이 지점을 시작점으로 하는 루프가 없다는 뜻이므로
# visit 리스트에 1을 맵핑해서 표시하고 True 리턴
# 그래프에 루프가 없다면 visit 리스트는 모두 1이 채워지면서 True만 반환되며 프로그램이 종료

numCourses = 3
prerequisites = [[0,1], [2,0], [1,2]]

# dfs detect cycle 
graph = collections.defaultdict(list)

# [0,1] 이라면 경로는 0 -> 1
for src, des in prerequisites:
    graph[src].append(des)
    
visit = [-1 for i in range(numCourses)]

def dfs(node):
    if visit[node] == 0: # 루프 경로가 있다
        return False
    
    if visit[node] == 1: # node에서 시작하는 루프 경로가 없다
        return True
    
    visit[node] = 0 # 방문 체크
    
    for nei in graph[node]:
        if not dfs(nei): 
            return False
    visit[node] = 1 # 1은 더 이상 루프가 없을 때
    return True

# 모든 노드에 대해 출발점으로 삼았을 때 루프가 있는지 탐색
for course in range(numCourses):
    if not dfs(course): 
        print(False)
        exit()
print(True)

# leetcode 제출용 코드

# class Solution(object):
#     def canFinish(self, numCourses, prerequisites):
#         """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#         """
        
#         # dfs detect cycle 
#         graph = collections.defaultdict(list)
#         for des, src in prerequisites:
#             graph[src].append(des)
            
#         visit = [-1 for i in range(numCourses)]
        
#         def dfs(node):
#             if visit[node] == 0: # 방문했다
#                 return False
            
#             if visit[node] == 1: # 방문 안했다?
#                 return True
            
#             visit[node] = 0 
            
#             for nei in graph[node]:
#                 if not dfs(nei): 
#                     return False
#             visit[node] = 1
#             return True
        
#         for course in range(numCourses):
#             if not dfs(course): 
#                 return False 
#         return True 
        
        
#         # 그래프가 순환되지 않으면서 모든 정점을 찍고 지나갈 수 있다면 true, 그렇지 않다면 False? 이게 맞나
        
#         graph = collections.defaultdict(list)
#         # 인접 리스트 생성
#         for x, y in prerequisites:
#             graph[x].append(y)
        
#         # 순환 구조를 판별하기 위해 이미 방문한 노드를 set에 저장
#         traced = set()
        
#         def dfs(i):
#             # 순환 구조이면 False
#             if i in traced:
#                 return False
            
#             traced.add(i)
#             for y in graph[i]:
#                 if not dfs(y):
#                     return False
                
#             # 탐색 종료 후 순환 노드 삭제
#             traced.remove(i)
            
#             return True
                
#         # 순환 구조 판별
#         for x in list(graph):       # 딕셔너리를 list()로 형변환하면 키만 담긴 리스트가 생성
#             if not dfs(x):
#                 return False
            
#         return True
    
    
    