class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        
        dict = collections.defaultdict(int)
        # 카운트를 세야 할 보석을 딕셔너리에 추가
        for jewel in jewels:
            dict[jewel] = 0
        
        # 보석 개수를 카운트
        for char in stones:
            if char in dict:
                dict[char] += 1
        
        # 카운트 한 보석을 모두 더해서 출력
        sum = 0
        for count in jewels:
            sum += dict[count]
            
        return sum
        