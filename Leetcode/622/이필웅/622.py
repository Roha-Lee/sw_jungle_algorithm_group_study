# LeetCode 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/

# 환형(원형 = 링버퍼) 큐 구현 문제

# 원래 큐에는 rear()라는 연산이 없다고 함. 

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.queue[self.rear] is None:
            self.queue[self.rear] = value
            self.rear = (self.rear+1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.queue[self.front] is None:
            return False
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True
        
    def Front(self) -> int:
        return -1 if self.queue[self.front] is None else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.queue[self.rear -1] is None else self.queue[self.rear -1]        

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is not None