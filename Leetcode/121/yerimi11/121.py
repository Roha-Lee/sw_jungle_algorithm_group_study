class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 한 번의 거래로 낼 수 있는 최대 이익 산출
        # 앞에서부터 작은 날에 사고 뒤에 높은 날에 팔기.. 오늘이 작은 줄 어떻게 알고? -> 리스트 값 다 계산해서 차이 보고 결정. min과 max구하기 (순서대로)
        profit = 0
        min_price = sys.maxsize
        
        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit
        
        # 시간복잡도 O(n)