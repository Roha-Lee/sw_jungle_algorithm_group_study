# LeetCode 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/

# 큐를 이용한 스택 구현 문제.

from collections import deque

class MyStack:
    # 시작 -> deque이용해서 q라는 데크 선언
    def __init__(self):
        self.queue = deque()
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        # 삽입 후에 맨앞으로 재정렬하는 구문
        for _ in range(len(self.q)-1):
            self.queue.append(self.q.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0