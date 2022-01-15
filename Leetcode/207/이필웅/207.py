# LeetCode 207.Course Schedule
# https://leetcode.com/problems/course-schedule/

# course Schedule 선행과목리스트가 주어지면 싸이클 유무 판단하는 문제

# Runtime : 113ms(61.28%)
# Memory Usage : 15.5MB(24.95%)

class Solution:
    def canFinish(self, n, prerequisites):
        G = [[] for i in range(n)]
        degree = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(n) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == n
