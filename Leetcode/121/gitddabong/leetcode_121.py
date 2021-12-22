prices = [7,1,5,3,6,4]

#         최소일 때 사서 최대로 팔면 되니까.
#         내가 보고있는 값보다 작은 수가 나오면 저장(최소 price)
#         최소 price보다 큰 수가 나올 경우 (현재 수 - 최소 price)를 profit에 저장

#         배열 다 돌고 나면 profit 출력
        
profit = 0
min_price = float('inf')
for price in prices:
    if min_price < price:
        profit = max(profit, price - min_price)
    
    else:
        min_price = price
        
print(profit)