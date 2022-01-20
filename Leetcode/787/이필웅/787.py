# LeetCode 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

# n(노드 갯수), flights 배열, src(시작점), dst(목적지), k(경유지점)
# 경유 지점 k개를 경유하는 가격을 리턴

import collections
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        if src == dst: return 0
        d, seen = collections.defaultdict(list), collections.defaultdict(lambda: float('inf'))
        for u, v, p in flights:
            d[u] += [(v, p)]
    
        q = [(src, -1, 0)]
        
        while q:
            pos, k, cost = q.pop(0)
            if pos == dst or k == K: continue 
            for nei, p in d[pos]:
                if cost + p >= seen[nei]:
                    continue
                else:
                    seen[nei] = cost+p
                    q += [(nei, k+1, cost+p)]
                
        return seen[dst] if seen[dst] < float('inf') else -1