# 121. Best Time to Buy and Sell Stock
[문제 링크](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
# 문제 
- `prices` 배열이 주어진다.
- `i`번째 인덱스이 값은 `i`번째 날 주식의 가격이다.
- 주식을 살 날과 주식을 팔 날을 하루씩만 선택하여 얻을 수 있는 이익 중 가장 큰 값을 반환하시오.
  - 만약 이익을 얻을 수 없는 경우 0을 출력하시오

# 문제 접근 방법
- for loop을 통해 주식의 최솟값과 그 때까지의 최대 이익을 갱신한다.

# 코드 1
- DP memoization을 이용한 풀이
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, float('inf')] for _ in range(len(prices))]
        dp[0][1] = prices[0]
        
        for i in range(1, len(prices)):
            prev_profit = dp[i-1][0]
            curr_profit =  prices[i] - dp[i-1][1]

            dp[i] = [max(prev_profit, curr_profit), min(dp[i-1][1], prices[i])]
                
        return dp[-1][0]
```

# 코드 2
- for loop을 통해 주식의 최솟값과 그 때까지의 최대 이익을 갱신하는 풀이
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            curr_profit = prices[i] - min_price
            max_profit = max(max_profit, curr_profit)
            
        return max_profit
```

# 시간 복잡도
  - O(N)