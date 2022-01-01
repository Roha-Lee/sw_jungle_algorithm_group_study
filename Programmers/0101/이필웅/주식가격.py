# Programmers 스택/큐 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

# 고찰과정
# 큰틀은 유사함. 어차피 하나의 인덱스에서 실행하면 그뒤의 값과 비교를 해야함
# 여기서 문제는 cnt 변수를 만들어서 주식가격이 떨어질 경우 cnt를 가산시키고 마지막에 append 시키는 방법으로 했는데
# 이러한 방법을 진행하면 효율성 테스트2를 통과하지 못함.
# 단순히 cnt변수를 만들고 append 시키는게 뭔가 시간 효율성 만족을 못시키는 것같았음.
# 그래서 길이만큼의 배열을 미리 만들고 해당 인덱스칸에 값을 가산시키는 방향으로 바꿨더니 바로통과됨.

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                answer[i] +=1
                break
            else: answer[i] += 1

    return answer

