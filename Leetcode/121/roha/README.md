# 121. Best time to buy and sell stock
[문제 링크](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
# 문제 요구 조건 
- 단 하루만을 골라서 주식을 살 수 있고, 그 이후에 팔 수 있다고 가정
- 최대 수익 구하기 
# 제한사항 
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`
# 풀이 
- next_max라는 리스트를 만든다. 
    - i번째 이후 등장하는 값들 중 가장 큰 값을 저장하는 리스트
    - prices를 역순으로 순회하여 값을 만들면 O(N)만에 만들어 낼 수 있다. 
- next_max는 판매가격이 들어있고 prices는 구매가격이 들어있으므로 두 리스트의 각 원소의 차이값 중에서 최소값을 반환한다. 
 