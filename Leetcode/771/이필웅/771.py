# LeetCode 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

# 보석과 돌이 있다. J는 보석이며, S는 갖고 있는 돌인 경우 S에는 보석이 몇개가 있는지?

# Runtime : 53ms(5.92%)
# Memory Usage : 14.2MB(46.04%)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {}
        for i in jewels:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        cnt = 0
        for j in stones:
            if j in dic:
                cnt +=1
        
        return cnt

# 더 나은 풀이
# set 이용하여 중복없는 형태로 변경

# Runtime : 28ms (85.42%)
# Memory Usage : 14MB (91.53%)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {}
        j = set(jewels)
        cnt = 0
        
        for i in stones:
            if i in j:
                cnt +=1
        
        return cnt