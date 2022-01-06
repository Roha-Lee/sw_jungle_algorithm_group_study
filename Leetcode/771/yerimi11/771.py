class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # stones에 jewels가 몇 개 있는지. 대소문자 구별
        stone_cnt = collections.Counter(stones)
        count = 0
        
        for jewel in jewels:
            count += stone_cnt[jewel]
            
        return count
        