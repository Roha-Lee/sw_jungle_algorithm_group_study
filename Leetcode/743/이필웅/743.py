# LeetCode 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

import collections, heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        Q = [(0,k)]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt,v))

        if len(dist) == n:
            return max(dist.values())
        return -1

a = Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2)

print(a)